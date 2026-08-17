# Technical SEO Audit Report

**เว็บไซต์**: เสื้อแท้.com (`https://xn--o3c1bj3b4bj8cd.com/`)  
**Codebase**: Shirt-manufacturing — Astro Static Site  
**วันที่ตรวจ**: 17 สิงหาคม 2026  
**ขอบเขต**: ตรวจ Source Code และไฟล์ Production Build ภายในเครื่อง (Pre-deployment Code Audit)  
**Provisional Score**: **76/100** (คะแนนเฉพาะ Codebase และ Local Production Build)  
**สถานะโดยรวม**: โครงสร้าง Technical SEO ระดับโค้ดอยู่ในเกณฑ์ดี แต่คะแนนนี้ยังไม่ใช่ Final Production Score จนกว่าจะตรวจเว็บไซต์ Production, Lighthouse/Core Web Vitals, Redirect และ Google Search Console

---

## Executive Summary

ระบบ SEO หลักถูกวางโครงสร้างไว้ค่อนข้างครบ ได้แก่ title, meta description, canonical, robots directives, sitemap, Open Graph, Twitter Card และ JSON-LD โดยรวมศูนย์ผ่าน `Layout.astro` และ `SEO.astro` ทำให้ดูแลได้ง่ายและลดความเสี่ยงจาก meta tag ซ้ำ

การตรวจ Production Build จำนวน 66 หน้าไม่พบหน้าที่ขาด `<title>`, meta description, canonical หรือ `<h1>` และ JSON-LD ทุกบล็อกสามารถ parse เป็น JSON ได้ อย่างไรก็ตาม รายงานนี้ยังไม่ยืนยันผลด้านความเร็วจริง, Core Web Vitals, HTTP status, redirect, indexation และ Rich Result eligibility เพราะหัวข้อเหล่านี้ต้องตรวจบนเว็บไซต์ที่ deploy แล้วหรือใช้ข้อมูลจาก Google

### Scorecard ตาม Technical SEO Checklist ของทีม

| หมวด | คะแนน | สถานะ |
|---|---:|---|
| Crawlability | 82/100 | Build ผ่าน; ยังไม่ได้ตรวจ X-Robots-Tag และ Production HTTP |
| Indexation | 75/100 | Meta/canonical ผ่าน; ยังไม่มี status-code crawl และ GSC |
| Performance | 62/100 | Architecture ดี; ยังไม่มี CWV, TTFB, cache/CDN และ bundle report |
| Mobile | 70/100 | มี responsive foundation; ยังไม่มี device/accessibility test ครบ |
| Security | 55/100 | ไม่พบ sensitive files ใน build; ยังไม่ได้ตรวจ HTTPS/headers |
| Structured Data | 82/100 | JSON syntax ผ่าน; ยังไม่ได้ตรวจ Rich Results eligibility |
| International SEO | 100/100 | เว็บไซต์ภาษาไทยภาษาเดียว; `lang="th"` ถูกต้องและ hreflang ไม่จำเป็น |
| URL Structure | 82/100 | โครงสร้างส่วนใหญ่ดี; ยังมี taxonomy/internal-link inconsistency |
| **ค่าเฉลี่ย** | **76/100** | **Provisional — ต้อง re-score หลัง Live Audit** |

### วิธีให้คะแนน

- ให้คะแนนเฉพาะสิ่งที่มีหลักฐานจาก Source Code หรือ `dist/`
- รายการที่ต้องตรวจบน Production แต่ยังไม่ได้ตรวจ จะไม่ถูกนับว่า “ผ่าน”
- คะแนนแต่ละหมวดให้น้ำหนักเท่ากันตาม 8 หมวดใน Technical SEO Checklist ของทีม
- เมื่อมี Live Audit ให้แทนที่คะแนน provisional ด้วยผล HTTP crawl, Lighthouse/CrUX, Rich Results Test และ Google Search Console

### ผลตรวจที่ยืนยันแล้ว

- `npm run build`: ผ่าน — สร้าง Static HTML 66 หน้า
- `npx astro check`: ผ่าน — 0 errors และมี 43 hints
- `npm run lint`: ไม่ผ่าน — พบ 7 errors
- HTML 66 หน้า: มี title, description, canonical และ H1 หนึ่งชุดครบทุกหน้า
- JSON-LD: parse ผ่านทุกบล็อก ไม่พบ JSON syntax error
- Sitemap: ไม่พบ URL `/tag/` และ `/blog-previews.json`
- Tag pages: เรนเดอร์ `noindex, nofollow`
- `robots.txt`: สร้างสำเร็จและอ้างอิง sitemap
- ไม่พบ `.env`, `.env.production` หรือ `.git` ภายใน `dist/`

> หมายเหตุ: ผลด้านบนยืนยันเฉพาะไฟล์ที่ build ภายในเครื่อง ไม่ได้ยืนยันว่า Hosting ส่งไฟล์หรือ HTTP headers เหมือนกันทุกประการ

---

## 1. Crawlability — 82/100

**สถานะ: ผ่านในระดับ Production Build / ต้องยืนยันบน Production**

### สิ่งที่ตรวจพบ

- `dist/robots.txt` ถูกสร้างจริง โดยอนุญาตให้ crawler เข้าถึงเว็บไซต์และบล็อก URL ที่มี query string ด้วย `Disallow: /*?`
- robots.txt อ้างอิงทั้ง `sitemap-index.xml` และ `sitemap-0.xml`
- `dist/sitemap-index.xml` และ `dist/sitemap-0.xml` ถูกสร้างสำเร็จ
- Sitemap กรอง `/tag/*` ซึ่งตั้ง `noindex` และ endpoint `/blog-previews.json` ออกแล้ว
- หน้า Tag ไม่ถูกบล็อกด้วย robots.txt ทำให้ crawler ยังเข้าถึงหน้าเพื่ออ่าน meta `noindex` ได้

### ข้อสังเกต

- การอ้างทั้ง sitemap index และ sitemap ลูกใน robots.txt ไม่ผิด แต่ซ้ำซ้อน โดยทั่วไปอ้างเฉพาะ sitemap index ก็เพียงพอ
- `Disallow: /*?` ช่วยลดการ crawl URL parameters แต่ crawler จะไม่เห็น canonical/noindex ภายใน URL parameter ที่ถูกบล็อก จึงควรใช้เมื่อมั่นใจว่า parameter URLs ไม่มีหน้าที่ต้องให้ Google crawl
- ยังไม่ได้ตรวจว่า `/robots.txt` และ sitemap ตอบ HTTP 200 บน Production จริง

### ผลประเมิน

โครงสร้าง Crawlability ใน build ถูกต้อง แต่ยังไม่ควรสรุปว่า Production ผ่านจนกว่าจะตรวจ HTTP response จริง

---

## 2. Indexation — 75/100

**สถานะ: ผ่านในระดับ HTML ที่ Build**

### สิ่งที่ตรวจพบ

- HTML ทั้ง 66 หน้ามี `<title>` หนึ่งชุด
- HTML ทั้ง 66 หน้ามี meta description หนึ่งชุด
- HTML ทั้ง 66 หน้ามี canonical หนึ่งชุด
- HTML ทั้ง 66 หน้ามี `<h1>` หนึ่งชุด
- หน้าเนื้อหาหลักเรนเดอร์เป็น index/follow ตามค่าเริ่มต้น
- หน้า `/tag/*` และหน้า 404 ตั้ง `noindex, nofollow`
- Canonical สร้างจาก `Astro.url.pathname` และ `Astro.site` จึงเป็น absolute URL และ self-referencing
- เว็บไซต์เป็น Static Site Generation ทำให้เนื้อหาหลักอยู่ใน HTML โดยไม่ต้องพึ่ง client-side JavaScript

### ข้อจำกัดของการตรวจ

- ยังไม่ได้ตรวจ Google Search Console ว่าหน้าใดถูก index, excluded, crawled หรือ discovered จริง
- ยังไม่ได้ตรวจ canonical ที่ Google เลือก (`Google-selected canonical`)
- ยังไม่ได้ตรวจ soft 404, orphan pages และ duplicate content ด้วย crawler ภายนอก
- Status code ของ Static HTML ขึ้นอยู่กับการตั้งค่า Hosting โดยเฉพาะหน้า 404
- ยังไม่ได้ตรวจ 200, 301, 302, 404, 410, 5xx, redirect chains และ redirect loops บน Production
- ยังไม่ได้ตรวจ `X-Robots-Tag` จาก HTTP response headers
- เว็บไซต์ไม่มี pagination ในหน้าหลักที่ตรวจ จึงไม่มีกรณี `rel="next/prev"` ที่ต้องประเมินในปัจจุบัน

---

## 3. URL Structure — 82/100

**สถานะ: ผ่านบางส่วน / มีจุดที่ควรปรับปรุง**

### สิ่งที่ทำได้ดี

- Sitemap มีเฉพาะหน้าที่ตั้งใจให้ค้นพบ และกรอง Tag pages กับ JSON endpoint ออก
- URL ของหน้าสินค้าและบทความส่วนใหญ่เป็นภาษาอังกฤษตัวพิมพ์เล็กและใช้ขีดกลางคั่นคำ
- Canonical ใช้รูปแบบ trailing slash สอดคล้องกับ output แบบ directory ของ Astro

### จุดที่ควรปรับปรุง

1. Sitemap ตั้ง `lastmod: new Date()` ให้ทุก URL ทุกครั้งที่ build ทำให้ทุกหน้าดูเหมือนถูกแก้ไขล่าสุดพร้อมกัน แม้เนื้อหาไม่ได้เปลี่ยนจริง ควรใช้วันที่แก้ไขจาก content หรือไม่ส่ง `lastmod` หากไม่มีข้อมูลที่เชื่อถือได้
2. Category URLs ใช้ภาษาไทย ซึ่งไม่ผิดหลัก SEO แต่ไม่ตรงกับข้อสรุปว่า URL ทั้งหมดเป็นภาษาอังกฤษ
3. มี Tag URL ที่ใช้ `DTF` ตัวพิมพ์ใหญ่ แม้ Tag pages ถูกนำออกจาก sitemap แล้วก็ตาม
4. พบ internal link บางแห่ง เช่นลิงก์กลับ `/blog` ในหน้า Tag ที่ไม่มี trailing slash การไม่มี slash ไม่ได้ทำให้เกิด redirect loop โดยตัวมันเอง แต่อาจเพิ่ม redirect หนึ่งครั้ง ขึ้นอยู่กับ Hosting

### URL depth และอักขระ

- URL หลักมีความลึกไม่เกินประมาณ 2–3 ระดับ เช่น `/products/<slug>/` และ `/blog/<slug>/`
- Slug ของสินค้าและบทความส่วนใหญ่ใช้ hyphen และไม่มีช่องว่าง
- Category และ Tag ใช้อักขระภาษาไทยซึ่ง browser จะ percent-encode การใช้ภาษาไทยไม่ใช่ข้อผิดพลาด แต่ควรกำหนดมาตรฐานให้สม่ำเสมอ

---

## 4. Performance — 62/100

**สถานะ: โครงสร้างระดับโค้ดดี / ยังให้คะแนน Production Performance ไม่ได้**

### สิ่งที่ตรวจพบ

- ภาพเนื้อหาส่วนใหญ่ใช้ `<Image>` จาก `astro:assets`
- Production Build สร้าง optimized image assets จำนวน 344 รายการ และผล build ที่ตรวจพบเป็น WebP
- รูปภาพที่ใช้ผ่าน Astro Image มี width/height ช่วยลดความเสี่ยง CLS
- React island สำหรับระบบค้นหา/กรองบทความใช้ `client:visible`
- เว็บไซต์ใช้ Static HTML เป็นหลัก
- Ahrefs Analytics โหลดแบบ `async`
- Google Analytics ถูกเลื่อนโหลดจนเกิด interaction หรือ browser idle
- Microsoft Clarity สร้าง script แบบ async แต่เริ่มโหลดตั้งแต่ initial page load
- Astro/Vite ทำ minification และ asset hashing ใน Production Build

### ข้อสังเกต

- ยังมี `<img>` แบบดิบในส่วน React Blog Explorer และ lightbox แต่เป็นกรณี dynamic image ไม่ได้หมายความว่าเป็น SEO error โดยอัตโนมัติ
- การใช้ optimized images และ deferred hydration ช่วยลดความเสี่ยงด้าน performance แต่ไม่สามารถใช้ยืนยันคะแนน LCP, INP, CLS หรือ TBT ได้
- Third-party scripts ได้แก่ Ahrefs, Google Analytics และ Microsoft Clarity อาจมีผลต่อ main thread, network และ privacy จึงต้องวัดบน Production

### รายการจาก Checklist ที่ยังไม่ได้ยืนยัน

- LCP < 2.5 วินาที, INP < 200 มิลลิวินาที และ CLS < 0.1
- TTFB < 200 มิลลิวินาที
- Brotli/gzip compression, browser caching headers และ CDN
- HTTP/2 หรือ HTTP/3
- Render-blocking resources และ font loading จากผล waterfall จริง
- Bundle size และ unnecessary dependencies ด้วย bundle analyzer

### สิ่งที่ยังต้องทดสอบ

- Lighthouse Mobile และ Desktop อย่างน้อย 3 รอบต่อหน้าหลัก
- PageSpeed Insights หรือ CrUX สำหรับข้อมูลผู้ใช้จริง
- หน้าแนะนำสำหรับทดสอบ: `/`, `/services/`, `/products/`, Product detail, `/blog/` และ Article detail
- ตรวจ LCP image, unused JavaScript, font loading, cache headers และ total transfer size

---

## 5. Mobile — 70/100

**สถานะ: ตรวจโครงสร้างเบื้องต้นแล้ว / ยังไม่ผ่านการทดสอบครบถ้วน**

### สิ่งที่ยืนยันได้

- มี viewport meta ที่ถูกต้อง
- CSS ใช้ responsive utilities หลาย breakpoint
- หน้าใน build มี H1 ครบ
- ปุ่ม Back to Top มี `aria-label`
- ภาพหลักส่วนใหญ่มี alt text

### สิ่งที่ยังยืนยันไม่ได้จาก Source Code เพียงอย่างเดียว

- ไม่มี horizontal overflow ทุก viewport
- Touch target ทุกจุดมีขนาดอย่างน้อย 44×44 CSS pixels
- Body text ทุกตำแหน่งมีขนาดอย่างน้อย 16px และอ่านได้โดยไม่ zoom
- ไม่มี intrusive interstitials ในทุก user journey
- Color contrast ผ่าน WCAG ทุก component และทุก state
- Keyboard navigation, focus order, modal focus trap และ screen reader behavior ถูกต้อง

ควรทดสอบอย่างน้อยที่ความกว้าง 320, 360, 390, 768, 1024 และ 1440 pixels รวมถึง Lighthouse Accessibility และ keyboard-only navigation

---

## 6. Security — 55/100

**สถานะ: ตรวจได้เฉพาะไฟล์ใน Repository และ Build**

### สิ่งที่ตรวจพบ

- `.env` และ `.env.production` อยู่ใน `.gitignore`
- Git track เฉพาะ `.env.example` ไม่พบ `.env` จริงในรายการ tracked files
- ไม่พบ `.env`, `.env.production` หรือ `.git` ภายใน `dist/`
- มี third-party analytics ได้แก่ Ahrefs, Google Analytics และ Microsoft Clarity

### สิ่งที่ยังต้องตรวจบน Production

- HTTPS ทุกหน้าและ mixed content
- HTTP → HTTPS redirect
- HSTS header
- Content Security Policy
- Security headers อื่น เช่น `X-Content-Type-Options` และ Referrer Policy
- Cookie consent/privacy disclosure ให้สอดคล้องกับ analytics และ session recording ที่ใช้งาน
- ตรวจว่า analytics IDs และ script ที่ติดตั้งเป็นของบัญชี Production ที่ถูกต้อง

---

## 7. Structured Data — 82/100

**สถานะ: JSON syntax ผ่าน / ยังไม่ยืนยัน Rich Result eligibility**

### Schema ที่พบใน Production Build

- `Organization`: 66 หน้า
- `WebSite`: 66 หน้า
- `BlogPosting`: 38 หน้า
- `BreadcrumbList`: 51 หน้า
- `FAQPage`: 36 หน้า
- `Product`: 6 หน้า
- `Blog`: 1 หน้า
- `CollectionPage`: 4 หน้า
- `ItemList`: 1 หน้า
- `Service`: 1 หน้า โดยมี `LocalBusiness` อยู่ภายใน `provider`

### สิ่งที่ทำได้ดี

- JSON-LD ทุกบล็อก parse ผ่าน ไม่พบ JSON syntax error
- Organization และ WebSite ใช้ `@id` คงที่ ช่วยเชื่อม entity ระหว่างหน้า
- Product ใช้ราคาและสถานะ stock จาก content ของสินค้าแต่ละรายการ
- Product มี Offer, priceCurrency, availability และ itemCondition
- หน้าบทความมี BlogPosting และ BreadcrumbList
- หน้าบริการมี Service, LocalBusiness provider, OfferCatalog, BreadcrumbList และ FAQPage

### ข้อสังเกต

- ราคาสินค้ามีหลายค่า ได้แก่ 180, 220, 350, 490, 650 และ 950 บาท จึงไม่ควรสรุปรวมว่า Product schema ทั้งหมดมีราคา 490 บาท
- LocalBusiness ยังไม่มี `geo`, `openingHoursSpecification` และลิงก์ Google Business Profile/Facebook/Instagram ที่ยืนยันแล้ว
- การ parse JSON สำเร็จไม่เท่ากับผ่าน Google Rich Results Test หรือมีสิทธิ์แสดง Rich Result
- ควรตรวจ URL ตัวอย่างของ Product, Article, FAQ และ Service ผ่าน Schema Markup Validator และ Google Rich Results Test หลัง deploy

---

## 8. International SEO — 100/100 (N/A สำหรับ hreflang)

**สถานะ: ผ่านสำหรับเว็บไซต์ภาษาเดียว**

- `<html>` ใช้ `lang="th"` ถูกต้อง
- Open Graph locale ใช้ `th_TH`
- Structured Data ใช้ `inLanguage: th-TH`
- เว็บไซต์ที่ตรวจเป็นภาษาไทยภาษาเดียว จึงไม่จำเป็นต้องมี `hreflang`
- หากในอนาคตเพิ่มภาษาอื่น ต้องเพิ่ม language-specific URLs, self-referencing hreflang และ `x-default` ตามโครงสร้างที่เลือก
- รายงานนี้ไม่ได้ประเมินคุณภาพการแปลด้วยมนุษย์ เพราะยังไม่มีหน้า multi-language

---

## 9. Code และ Build Quality (หัวข้อเสริม)

**สถานะ: Build ผ่าน / Lint ไม่ผ่าน**

### ผลคำสั่งตรวจสอบ

- `npm run build`: ผ่าน
- `npx astro check`: 0 errors, 43 hints
- `npm run lint`: ไม่ผ่าน พบ 7 errors

### Lint errors ที่พบ

- `src/components/Navbar.astro`: explicit `any` 2 จุด
- `src/components/home/PriceCalculator.astro`: ตัวแปร `currentColor` ไม่ถูกใช้งาน
- `src/components/products/PortfolioCard.astro`: `description` และ `tags` ไม่ถูกใช้งาน
- `src/pages/products/index.astro`: import `SITE` ไม่ถูกใช้งาน
- `src/pages/services.astro`: ตัวแปร `works` ไม่ถูกใช้งาน

Lint errors เหล่านี้ไม่ใช่ Technical SEO blocker โดยตรง แต่ควรแก้เพื่อรักษาคุณภาพโค้ดและให้ CI สามารถตรวจจับ regression ได้

---

## 10. Git และ Audit Traceability (หัวข้อเสริม)

**สถานะ: ควรปรับปรุง**

- Repository ปัจจุบันมี commit เดียว (`3ff017b`) ชื่อ `ฝึฝึก Audit`
- Commit ดังกล่าวเพิ่มทั้งโปรเจกต์ 243 ไฟล์และประมาณ 23,374 บรรทัด ทำให้ไม่มี baseline สำหรับเปรียบเทียบก่อนและหลัง audit
- Repository pack มีขนาดประมาณ 121.67 MB เนื่องจากมี image assets จำนวนมาก
- ไฟล์ `MY-SEO-AUDIT-REPORT.md` ยังเป็น untracked ณ เวลาที่ตรวจ

### ข้อเสนอแนะ

- Commit รายงานแยกจากโค้ด เช่น `docs: add pre-deployment technical SEO audit`
- การแก้ SEO ในอนาคตควรแยก commit ตามประเด็น เพื่อย้อนตรวจเหตุผลและผลกระทบได้
- ในรายงานรอบถัดไปให้บันทึก commit SHA, URL, วันเวลา, tools, commands และผลก่อน/หลัง
- พิจารณาจัดเก็บ binary images ขนาดใหญ่ด้วย Git LFS หรือระบบ asset storage หาก repository โตต่อเนื่อง

---

## Priority Findings

### High — ต้องทำก่อนสรุปคะแนน SEO

1. **ตรวจ Production domain จริง** — HTTP status, HTTPS, www/non-www, trailing slash, canonical, robots.txt, sitemap และ redirect chain
2. **วัด Lighthouse/Core Web Vitals** — ห้ามสรุปคะแนน Performance หรือ Mobile จาก Source Code เพียงอย่างเดียว
3. **ตรวจ Indexation ใน Google Search Console** — Coverage/Page Indexing, selected canonical และ sitemap processing
4. **ตรวจ Structured Data ด้วยเครื่องมือภายนอก** — อย่างน้อย Product, Article, FAQ และ Service

### Medium — ควรปรับปรุง

1. ใช้ `lastmod` จากวันที่เนื้อหาแก้จริง แทน `new Date()` ทุกครั้งที่ build
2. เพิ่มข้อมูล LocalBusiness ที่ยืนยันแล้ว ได้แก่ geo, opening hours, Google Business Profile และ social profiles
3. ตรวจและทำ internal URL format ให้สม่ำเสมอ เพื่อลด redirect ที่ไม่จำเป็น
4. แก้ lint errors ทั้ง 7 จุดและเพิ่ม lint/build เป็น CI checks
5. ตรวจ privacy/cookie disclosure สำหรับ Analytics และ Microsoft Clarity

### Low — ปรับเพื่อความเรียบร้อย

1. อ้างเฉพาะ sitemap index ใน robots.txt เพื่อลดความซ้ำซ้อน
2. ทบทวนการใช้ภาษาไทยและตัวพิมพ์ใหญ่ใน taxonomy URLs ให้เป็นมาตรฐานเดียวกัน
3. ลด hints จาก `astro check` โดยเฉพาะ deprecated schema API และ unused declarations

---

## Final Assessment

เว็บไซต์มีพื้นฐาน Technical SEO ระดับโค้ดที่ดี โดยเฉพาะการรวม SEO metadata ไว้ส่วนกลาง, การสร้าง Static HTML, canonical, robots directives, sitemap, optimized images และ structured data หลายประเภท ผล build และ type-check ผ่าน และ HTML ที่สร้างมีองค์ประกอบ SEO พื้นฐานครบ

อย่างไรก็ตาม ยังไม่ควรระบุคะแนน 98/100 หรือเกรด A+ เพราะยังไม่มีหลักฐานจาก Production crawl, Lighthouse/Core Web Vitals, Google Search Console และ Rich Results Test รวมถึง lint ยังไม่ผ่านและ sitemap `lastmod` ยังไม่สะท้อนวันที่แก้ไขจริง

**ข้อสรุปที่ถูกต้อง ณ ตอนนี้**: “ได้คะแนน Provisional Technical SEO 76/100 จาก Codebase และ Local Production Build โครงสร้างพื้นฐานอยู่ในเกณฑ์ดี แต่ต้องผ่าน Live Production Validation ก่อนกำหนดคะแนนขั้นสุดท้าย”

---

## หลักฐานและคำสั่งที่ใช้ตรวจ

```bash
git status --short
git log --oneline --decorate
npm run build
npx astro check
npm run lint
```

ตรวจเพิ่มเติมจากไฟล์ใน `dist/`:

- จำนวน HTML ที่ build
- จำนวน title, description, canonical และ H1 ต่อหน้า
- JSON syntax ของ `<script type="application/ld+json">`
- robots.txt และ sitemap output
- การไม่มี `/tag/` และ `/blog-previews.json` ใน sitemap
- การไม่มี `.env` และ `.git` ใน Production Build
