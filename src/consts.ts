// ค่าคงที่กลางของเว็บ — แก้ที่เดียว ใช้ได้ทั้งไซต์ (SEO, RSS, JSON-LD)
export const SITE = {
  name: 'รับผลิตเสื้อยืด.com',
  title: 'รับผลิตเสื้อยืด.com — โรงงานรับผลิตเสื้อครบวงจร สกรีน ตัดเย็บ ออกแบบฟรี',
  description:
    'รับผลิตเสื้อยืด.com โรงงานรับผลิตเสื้อยืด โปโล แจ็คเก็ต เสื้อช็อป และกระเป๋าผ้า ครบจบในที่เดียว โดย บริษัท ธน พลัส 153 จำกัด พร้อมงานสกรีน ออกแบบฟรี',
  // ภาษาเริ่มต้นของไซต์
  lang: 'th',
  locale: 'th_TH',
  // รูป Open Graph เริ่มต้น (วางไฟล์จริงไว้ที่ public/og-default.png)
  defaultOgImage: '/og-default.png',
  // ข้อมูลองค์กรสำหรับ JSON-LD
  author: 'บริษัท ธน พลัส 153 จำกัด',
  contact: {
    phone: '090-201-9121',
    phoneLink: 'tel:0902019121',
    line: '@thanaplus',
    lineLink: 'https://line.me/R/ti/p/%40thanaplus',
    email: 'thanaplusonline@gmail.com',
    address: '503 ถนนสุโขทัย แขวงสวนจิตรลดา เขตดุสิต กรุงเทพมหานคร 10300',
  },
} as const;

