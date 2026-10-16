# กระบวนการ agent ทำแทนและสัญญาสคริปต์ — powpow-register

รายละเอียดการทำงานของแต่ละขั้นใน SKILL.md คำสั่งทั้งหมดอยู่ในรูป `node scripts/powpow-register.mjs <คำสั่งย่อย> [พารามิเตอร์]`
สคริปต์ **ไร้ dependencies ต้องมี Node ≥ 18** และ request ทั้งหมดส่งไปที่ `https://global.powpow.online` เท่านั้น

## ดีไซน์ความปลอดภัย (ทำไมถึงออกแบบแบบนี้)

| ดีไซน์ | เหตุผล |
|---|---|
| รหัสผ่านส่งเข้ามาทางตัวแปรสภาพแวดล้อม `POWPOW_REGISTER_PASSWORD` เท่านั้น | พารามิเตอร์บรรทัดคำสั่งของโพรเซสมองเห็นได้จากโพรเซสอื่นบนเครื่องเดียวกัน (ช่องรั่ว argv) ส่วนตัวแปรสภาพแวดล้อมสคริปต์อ่านแล้วใช้ทันที |
| รหัสผ่าน **ห้ามเขียนลงไฟล์สถานะเด็ดขาด** ห้ามปรากฏใน log | ไฟล์สถานะอาจค้างอยู่บนดิสก์ ส่วนการแสดงครั้งเดียวในโหมดสร้างรหัสทำเพื่อให้ผู้ใช้ได้บันทึก |
| ไฟล์สถานะเก็บในไดเรกทอรี temp ของระบบ (`os.tmpdir()/powpow-register-state.json`, 0600) | มีแค่ห้าฟิลด์ email / username / nickname / token / outTradeNo และ `cleanup` เคลียร์ในคำสั่งเดียว |
| JWT ที่ agent ได้มาแลกเป็น cookie ของเบราว์เซอร์ผ่าน endpoint ทางการ `me?token=` | สะพานทางการที่แพลตฟอร์มออกแบบไว้สำหรับ WebView ของ HarmonyOS การตรวจลายเซ็นดูแค่ลายเซ็น+อายุ ไม่ผูกกับลายนิ้วมืออุปกรณ์ เบราว์เซอร์ของผู้ใช้จึงใช้ได้ |
| การจ่ายเงินทำแค่ create-order / query / เปิดหน้าชำระเงิน | การกระทำจ่ายเงินและหลักฐานการจ่ายอยู่ระหว่างผู้ใช้กับหน้าชำระเงินทางการของ Alipay เสมอ agent ไม่แตะต้อง |

## คู่มือคำสั่ง

| คำสั่ง | พารามิเตอร์สำคัญ | หน้าที่ / จังหวะที่ใช้ |
|---|---|---|
| `status` | —— | ดูความคืบหน้ากระบวนการ (อ่านไฟล์สถานะ) หลังบทสนทนาถูกตัดให้รันอันนี้ก่อน |
| `gen-password` | —— | สร้างรหัสผ่านแข็งแรง 24 ตัวอักษร (มีทั้งพิมพ์ใหญ่+พิมพ์เล็ก+ตัวเลข) stdout แสดง **ครั้งเดียวเท่านั้น** |
| `prepare-suggest` | `--username --nickname --email` | จดข้อมูลที่ยืนยันแล้วลงไฟล์สถานะ (หลังจากนี้ register ไม่ต้องส่งซ้ำ) |
| `send-code` | `--email` | กระตุ้นแพลตฟอร์มให้ส่งรหัสยืนยัน 6 หลัก (อยู่ 10 นาที คูลดาวน์ 60 วิ) |
| `register` | `--code` (จำเป็น); `--username --nickname --avatar --phone` (ไม่จำเป็น ถ้าไฟล์สถานะมีแล้วไม่ต้องส่ง) | สร้างบัญชี pending รหัสผ่านผ่านตัวแปรสภาพแวดล้อม `POWPOW_REGISTER_PASSWORD` สำเร็จแล้ว JWT ถูกเก็บลงไฟล์สถานะอัตโนมัติ |
| `login-link` | `--target pending` หรือ `--target home` | สร้างลิงก์ล็อกอินคลิกเดียว (ดีไซน์สองลิงก์ ดูด้านล่าง) |
| `create-order` | `--package monthly\|quarterly\|yearly` (ค่าเริ่มต้น Alipay)<br>`--provider alipay\|paypal` | สร้างออเดอร์จ่ายเงิน Alipay คืน path ไฟล์หน้าจ่ายเงิน + outTradeNo; PayPal คืน path ไฟล์หน้าอนุมัติ + subscriptionId (จดลงไฟล์สถานะอัตโนมัติ) |
| `query` | —— | เช็กสถานะออเดอร์/สมาชิก Alipay: `paid / pending / closed / unknown`; PayPal: `ACTIVE / PENDING`; โพลทุก 10–15 วิ |
| `refresh-login` | รหัสผ่านผ่านตัวแปรสภาพแวดล้อม | ล็อกอินใหม่เพื่อ **JWT ใหม่** (claim สมาชิกเปลี่ยนจาก NONE เป็น ACTIVE) ต้องรันหลังเงินเข้าเสมอ |
| `whoami` | —— | ใช้ token ในไฟล์สถานะเช็กบัญชีและสถานะสมาชิก (ยืนยันว่าเปิดใช้งานได้ผลหรือไม่) |
| `cleanup` | —— | ลบไฟล์สถานะ (ต้องรันตอนเก็บกวาด) |

**การส่งตัวแปรสภาพแวดล้อม** (รหัสผ่านห้ามขึ้นบรรทัดคำสั่งเด็ดขาด):

```bash
# bash / zsh / WSL
POWPOW_REGISTER_PASSWORD='<รหัสผ่าน>' node scripts/powpow-register.mjs register --code 123456
# PowerShell
$env:POWPOW_REGISTER_PASSWORD = '<รหัสผ่าน>'; node scripts/powpow-register.mjs register --code 123456
# cmd
set POWPOW_REGISTER_PASSWORD=<รหัสผ่าน> && node scripts/powpow-register.mjs register --code 123456
```

## กลไกสองลิงก์ (ดีไซน์แกนหลัก)

สถานะล็อกอินของแพลตฟอร์มคือ cookie แบบ HttpOnly agent ปลูก cookie แทนเบราว์เซอร์คนอื่นโดยตรงไม่ได้
สะพานคือ endpoint ทางการ `/api/auth/me?token=<JWT>&redirect=<เส้นทางในไซต์>`: ตรวจลายเซ็น → ผู้ใช้ pending
ได้รับการสร้าง session ให้อัตโนมัติ → `Set-Cookie: powpow_token` (HttpOnly / SameSite=Lax / 7 วัน) →
ตรวจสอบ redirect (ต้องขึ้นต้นสแลชตัวเดียว ห้าม `//` และแบ็กสแลช หลัง resolve แล้วต้อง same-origin) →
307 รีไดเรกต์ชั่วคราวไปหน้าปลายทาง

- **ลิงก์ 1 (ให้ทันทีหลังสมัครสำเร็จ)**: `--target pending` → ตกที่ `/subscription`
  เบราว์เซอร์ของผู้ใช้เข้าสู่สถานะ «ครึ่งเซสชัน»: หน้าแพ็กเกจสมาชิกและหน้าเด้งกลับของ Alipay เห็นและกดได้
  ส่วนหน้าเนื้อหายังโดนกำแพงค่าธรรมเนียมดันกลับมาหน้าแพ็กเกจสมาชิก (การป้องกันสามชั้น: เกตเวย์ตรวจ JWT claims →
  ตรวจซ้ำจาก DB → ตรวจที่ API หลัก เป็นพฤติกรรมปกติ)
- **ลิงก์ 2 (ให้หลังยืนยัน paid)**: ก่อนอื่น `refresh-login` เพื่อ JWT ใหม่ (การจ่ายเงินอัปเดตแค่ DB
  ไม่แก้ claims ของ JWT ที่ออกไปแล้ว ถ้าไม่เปลี่ยนใหม่จะดูเหมือน «จ่ายแล้วแต่ไม่มีสมาชิก») จากนั้น `--target home` →
  ตกหน้าแรก สถานะสมาชิกเต็มรูปแบบ

## ลำดับเวลาฉบับเต็ม (เส้นทางปกติ)

```
1.  status                          # ตรวจสภาพแวดล้อมตัวเอง
2.  (ขั้นที่ 2 ยืนยันข้อมูลในบทสนทนา รหัสผ่านเลือก 1 จาก 2; โหมดสร้าง: gen-password → ให้ผู้ใช้บันทึกทันที)
3.  prepare-suggest --username U --nickname N --email E
4.  send-code --email E             # → ผู้ใช้เข้าอีเมลดูรหัส (จุดออกจากบทสนทนาเดียว ①)
5.  POWPOW_REGISTER_PASSWORD=*** register --code 123456 [--avatar pic.jpg]
6.  login-link --target pending     # → ลิงก์ 1 ส่งให้ผู้ใช้
7.  (ผู้ใช้เลือกวิธีจ่ายเงิน)
    # Alipay: create-order --package monthly|quarterly|yearly
    # PayPal: create-order --provider paypal
8.  start <ไฟล์หน้าจ่ายเงิน>        # Windows; macOS ใช้ open, Linux ใช้ xdg-open
    # → ผู้ใช้จ่ายเงิน/อนุมัติที่หน้าชำระเงิน Alipay/PayPal (จุดออกจากบทสนทนา ②)
9.  query (ทุก 10–15 วิ) จนกว่าจะ paid / ACTIVE
10. refresh-login                   # ขอ JWT ใหม่พร้อม claim ACTIVE
11. login-link --target home        # → ลิงก์ 2 ส่งให้ผู้ใช้
12. whoami                          # ยืนยัน subscriptionStatus: ACTIVE (ไม่บังคับ)
13. cleanup                         # เคลียร์ไฟล์สถานะ
```

## การจับคู่คำสั่ง → API ของแพลตฟอร์ม

| คำสั่งสคริปต์ | API ของแพลตฟอร์ม |
|---|---|
| `send-code` | `POST /api/auth/register/send-code` |
| `register` | `POST /api/auth/register` (multipart, อัปโหลดรูปโปรไฟล์ตรง ๆ) |
| `login-link` | `GET /api/auth/me?token=…&redirect=…` (ตัวลิงก์เอง มีผลเมื่อเบราว์เซอร์คลิก) |
| `create-order` | `POST /api/payment/alipay/create-order` (Bearer, Alipay)<br>`GET /api/subscription/plans` + `POST /api/subscription/create` (Bearer, PayPal) |
| `query` | `GET /api/payment/alipay/query?outTradeNo=…` (Bearer, Alipay)<br>`GET /api/subscription/create` (Bearer, PayPal) |
| `refresh-login` | `POST /api/auth/login` (`{step:1, username, password}`) |
| `whoami` | `GET /api/auth/me?token=…` |

ที่มาของกฎ: ฟิลด์สมัครและเรตลิมิตดู `registration-flow.md` แพ็กเกจและห่วงโซ่เปิดใช้งานดู
`payment-and-activation.md` (ระบุไฟล์ซอร์สโค้ดของแพลตฟอร์มไว้ทั้งคู่)

## การจัดการ error ระดับสคริปต์

| อาการ | วิธีจัดการ |
|---|---|
| `เวอร์ชัน Node ต่ำเกินไป` | ถอยไปโหมดแนะนำล้วน อย่าฝืนรัน |
| เครือข่ายผิดพลาด / timeout | รีไทร์หนึ่งครั้ง ยังไม่ได้ให้ผู้ใช้เช็กเน็ตแล้วทำต่อ (ไฟล์สถานะยังอยู่ รัน `status` จากต้นเพื่อกู้คืน) |
| register โดน error เชิงธุรกิจ (ชื่อผู้ใช้มีอยู่แล้ว ฯลฯ) | จัดการตามตารางขั้นที่ 5 ใน SKILL.md **ไม่ต้องส่งรหัสยืนยันใหม่** (ยังใช้ได้อีก 10 นาที) |
| register แจ้ง 「邮箱验证码错误或已过期」 (รหัสยืนยันผิดหรือหมดอายุ) | หมดเวลา → `send-code` ใหม่ |
| หลัง `create-order` ผู้ใช้ปิดหน้าจ่ายเงิน | รัน `create-order` ใหม่ได้เลย (ออเดอร์เก่าปิดเองใน 2 ชม.; สมาชิก PENDING ของ PayPal หมดอายุใน 1 ชม.) |
| `create-order --provider paypal` คืน 409 | มีสมาชิก PayPal ที่ยังไม่เสร็จอยู่ รอ 1 ชม. ให้หมดอายุ หรืออนุมัติลิงก์เก่าในเบราว์เซอร์ |
| `query` เป็น pending / PENDING ตลอด | ผู้ใช้อาจยังไม่ได้จ่าย ถามสักคำ ถ้าจ่ายจริง → เดินตามตารางวินิจฉัยใน payment-and-activation.md |
| `refresh-login` 403 `pending_payment` | เงิน/การอนุมัติยังไม่เข้า กลับไปขั้นที่ 9 โพลต่อ |
| ไฟล์สถานะหาย (ลบพลาด / เปลี่ยนเครื่อง) | `whoami`/`refresh-login` ใช้ไม่ได้ ให้ผู้ใช้เปิดเบราว์เซอร์ที่เคยเปิดลิงก์ 1 แล้วรีเฟรชหน้าแพ็กเกจสมาชิกเพื่อดูสถานะ หรือล็อกอินใหม่ (โหมดหน้าเว็บ) |

## โหมดถอย (แนะนำล้วน)

เจอกรณีใดกรณีหนึ่งด้านล่างให้ถอยกลับไปโหมดแนะนำล้วนแบบ v1 ทันที เลิกยุ่งกับสคริปต์:

- ไม่มี Node ≥ 18 หรือสคริปต์พังชนิดเดียวกันสองครั้งติด;
- ผู้ใช้บอกชัดว่า «ฉันจะทำเองบนหน้าเว็บ»;
- นโยบายบริษัท/อุปกรณ์ห้ามสคริปต์ออกเน็ต

หลังถอย: ให้หน้าสมัคร https://global.powpow.online/register กับหน้าแพ็กเกจสมาชิก
https://global.powpow.online/subscription เดินตามกฎใน `registration-flow.md` น้ำเสียงเดิม
ทุกรอบยังปิดด้วยบล็อก «ก้าวต่อไป» เหมือนเดิม
