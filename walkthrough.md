# Walkthrough - ปรับปรุงโครงสร้างหน้าเว็บและระบบจัดการรูปภาพ

เราได้ทำการออกแบบโครงสร้างหน้าเว็บใหม่ทั้งหมดให้ดูมีความเป็นพรีเมียมสตูดิโอ (Boutique Editorial) เลี่ยงสไตล์เทมเพลต AI ทั่วไป และรวบรวมไฟล์ภาพให้อยู่ในที่เดียวกันเพื่อให้จัดการและค้นหาได้ง่ายขึ้น

---

## 1. การจัดระเบียบไฟล์ภาพ (Image Organization)

ไฟล์รูปภาพทั้งหมดที่เกี่ยวข้องกับการดีไซน์และการแสดงผล ถูกรวบรวมไว้ที่โฟลเดอร์โครงการเดียวกัน:
* **ที่อยู่โฟลเดอร์**: [src/assets/home/](file:///C:/Users/VICTUS/Desktop/ผลิตเสื้อ/astro-t_shirt/src/assets/home/)
* **ภาพที่สร้างขึ้นใหม่**:
  * [jacket_premium.png](file:///C:/Users/VICTUS/Desktop/ผลิตเสื้อ/astro-t_shirt/src/assets/home/jacket_premium.png) (เสื้อแจ็คเก็ตบอมเบอร์แคนวาสมินิมัล)
  * [class_tshirt.png](file:///C:/Users/VICTUS/Desktop/ผลิตเสื้อ/astro-t_shirt/src/assets/home/class_tshirt.png) (กองเสื้อยืดกิจกรรม)

---

## 2. หน้าเว็บตัวอย่างที่เชื่อมโยงกัน (Interlinked Preview Pages)

เราได้สร้างหน้าเพจต้นแบบ (Static Preview Pages) ครบถ้วนตามทุกแท็บเมนูของเว็บไซต์ และอัปเดตระบบลิงก์ในเมนู Navbar และ Footer ให้สามารถกดนำทางสลับหน้าได้อย่างลื่นไหลบน Live Server:

* [หน้าหลัก (Home) - ui-preview.html](file:///C:/Users/VICTUS/Desktop/ผลิตเสื้อ/astro-t_shirt/ui-preview.html)
* [หน้าบริการ (Services) - services-preview.html](file:///C:/Users/VICTUS/Desktop/ผลิตเสื้อ/astro-t_shirt/services-preview.html)
* [หน้าผลงาน (Products) - products-preview.html](file:///C:/Users/VICTUS/Desktop/ผลิตเสื้อ/astro-t_shirt/products-preview.html)
* [หน้าบทความ (Blog) - blog-preview.html](file:///C:/Users/VICTUS/Desktop/ผลิตเสื้อ/astro-t_shirt/blog-preview.html)

---

## 3. รายละเอียดดีไซน์พรีเมียม (Boutique Redesign Detail)

* **ตารางลายดราฟต์สิ่งทอ (Draft Grid Background)**: ลวดลายจางๆ ด้านหลัง เพิ่มสัมผัสของงานฝีมือและการถักทอผ้า
* **ดีไซน์ขอบเหลี่ยมเฉียบ (Flat Aesthetic)**: ปุ่ม เมนู และกรอบการ์ดตัดขอบเหลี่ยมเพื่อความเนี้ยบหรูหรา
* **โครงสร้างแบบสลับระยะเยื้อง (Alternating Asymmetry)**: เลี่ยงการวางกล่องบล็อกสี่เหลี่ยมสมมาตรธรรมดา ช่วยให้เนื้อหามีชีวิตชีวา น่าอ่านแบบนิตยสารแฟชั่น
