import { readFile, writeFile, mkdir } from 'node:fs/promises';
import { existsSync } from 'node:fs';
import path from 'node:path';
import Replicate from 'replicate';

const ROOT = process.cwd();
const ASSET_DIR = path.join(ROOT, 'src', 'assets', 'home');

async function loadEnv() {
  const envPath = path.join(ROOT, '.env');
  if (!existsSync(envPath)) return;
  const raw = await readFile(envPath, 'utf8');
  for (const line of raw.split(/\r?\n/)) {
    const m = line.match(/^\s*(?:export\s+)?([A-Za-z0-9_]+)\s*=\s*(.*)\s*$/);
    if (!m) continue;
    let val = m[2].trim();
    if ((val.startsWith('"') && val.endsWith('"')) || (val.startsWith("'") && val.endsWith("'"))) {
      val = val.slice(1, -1);
    }
    if (!(m[1] in process.env)) process.env[m[1]] = val;
  }
}

async function main() {
  await loadEnv();
  
  if (!process.env.REPLICATE_API_TOKEN) {
    console.error('✗ ไม่พบ REPLICATE_API_TOKEN ใน .env');
    process.exit(1);
  }

  const prompt = 'A premium black canvas bomber jacket, front view, hanging on a wooden hanger, against a clean minimalist light cream studio wall background, professional e-commerce product photography, high-quality, matching style, soft diffused lighting, no person';
  console.log(`▶ Generating front view jacket image using Replicate: "${prompt}"`);

  const replicate = new Replicate();
  const output = await replicate.run('black-forest-labs/flux-2-pro', {
    input: {
      prompt: prompt,
      aspect_ratio: '3:4',
      output_format: 'png',
      safety_tolerance: 5
    }
  });

  const file = Array.isArray(output) ? output[0] : output;
  const url = typeof file === 'string'
    ? file
    : (typeof file?.url === 'function' ? String(file.url()) : String(file));

  console.log(`▶ Downloading generated image from: ${url}`);
  const res = await fetch(url);
  if (!res.ok) {
    console.error(`✗ Download failed: HTTP ${res.status}`);
    process.exit(1);
  }
  const buf = Buffer.from(await res.arrayBuffer());

  await mkdir(ASSET_DIR, { recursive: true });
  const outPath = path.join(ASSET_DIR, 'jacket_front.png');
  await writeFile(outPath, buf);

  console.log(`✓ Saved generated image to: src/assets/home/jacket_front.png (${(buf.length / 1024).toFixed(0)} KB)`);
}

main().catch((e) => {
  console.error('✗ Error:', e?.message || e);
  process.exit(1);
});
