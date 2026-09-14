# ProPaymun Information Architecture

[![Version](https://img.shields.io/badge/version-1.0.1-5B4BDB)](CHANGELOG.md)
[![License](https://img.shields.io/badge/license-MIT--0-2F855A)](LICENSE)
[![Agent Skill](https://img.shields.io/badge/Agent%20Skill-ready-111827)](SKILL.md)

توضیحات عادی محصول را به معماری اطلاعات، سایت‌مپ محصول و یوزرفلوی روشن، شواهدمحور و قابل‌تصمیم‌گیری تبدیل می‌کند؛ حتی اگر کاربر اصطلاحات تخصصی را نداند.

نام رسمی محصول **ProPaymun** است. کامل‌بودن اینجا یعنی معماری قابل‌فهم، آمادهٔ تصمیم و صادق دربارهٔ مجهولات؛ نه یک سند طولانی و غیرضروری.

[English](README.md)

## بسته مناسب را انتخاب کنید

برای یک فایل مشترک در گفت‌وگوهای فایل‌پذیر، Projects و Gemini Gems از [فایل Markdown مهارت](packages/workspace-kit/propaymun-ia-workspace-kit.md) استفاده کنید. ابتدای همین فایل، دستور کوتاه تنظیم محیط آمده است. برای نصب بومی در Claude Skills از ZIP استفاده کنید؛ آن ZIP را در Knowledge جمینای قرار ندهید. روش معماری اطلاعات در هر دو بسته از یک منبع ساخته می‌شود؛ فایل Markdown ابزارهای اجرایی Python را همراه ندارد.

جریان مکالمه به ابزار نیاز ندارد. ابزارهای اختیاری Python برای اعتبارسنجی JSON معماری، سایت‌مپ محصول یا یوزرفلو، تولید HTML معماری یا خروجی Builder فقط در پاسخ به درخواست استفاده می‌شوند و به شبکه یا اطلاعات ورود دسترسی ندارند. نصب مهارت مجوز اجرای اسکریپت، ساخت فایل یا تغییر حافظهٔ پایدار نیست؛ کنترل دسترسی محیط میزبان برقرار می‌ماند. ابزار ساخت بسته در فایل نصب کاربران قرار ندارد. [محدوده و محدودیت‌های امنیتی](SECURITY.md)

| بسته | مناسب برای | دریافت |
|---|---|---|
| **بسته Agent Skill** | Claude.ai Skills و فقط محیط‌هایی که مستندات خودشان سازگاری با بستهٔ Agent Skill را تأیید کرده‌اند | [دانلود ZIP](packages/agent-skill/propaymun-information-architecture.zip) |
| **کیت Workspace** | ChatGPT Projects، Claude Projects، Gemini Gemهایی که دستی ساخته می‌شوند و محیط‌هایی با Instructions پایدار و فایل Knowledge | [فایل دانش](packages/workspace-kit/propaymun-ia-workspace-kit.md) + [دستور Workspace](packages/workspace-kit/WORKSPACE_INSTRUCTIONS.md) |

هر دو بسته از یک رفتار اصلی ساخته می‌شوند. فعال‌شدن خودکار، ماندگاری، ابزارها و محدودیت Context به سرویس میزبان وابسته است.

## نصب در Claude.ai

1. **[بسته Agent Skill](packages/agent-skill/propaymun-information-architecture.zip)** را دانلود کنید.
2. در Claude.ai، قابلیت **Settings → Capabilities → Code execution and file creation** را فعال کنید.
3. وارد **Customize → Skills** شوید.
4. مسیر **+ → Create skill → Upload a skill** را انتخاب کنید.
5. فایل ZIP را بدون Extract کردن آپلود و Skill را فعال کنید.

لینک مخزن GitHub فایل قابل‌آپلود Claude.ai نیست؛ از ZIP بالا استفاده کنید.

## راه‌اندازی در Workspaceهای وب

برای محیطی که صریحاً هم Instructions پایدار و هم فایل Knowledge دارد:

1. فایل [`propaymun-ia-workspace-kit.md`](packages/workspace-kit/propaymun-ia-workspace-kit.md) را به دانش Workspace اضافه کنید؛
2. دستور کوتاه ابتدای همان فایل را در Instructions محیط قرار دهید؛ [دستور مستقل Workspace](packages/workspace-kit/WORKSPACE_INSTRUCTIONS.md) فقط جایگزین مفصل‌تر است و فایل دانش دوم لازم نیست؛
3. با زبان طبیعی معماری اطلاعات، سایت‌مپ محصول/UX یا یوزرفلو بخواهید.

این مسیر «تنظیم با دانش پروژه» است و نباید به‌اشتباه نصب Native Skill نامیده شود.

### Gemini وب

Gemini وب این بسته را به‌صورت Native Skill نصب نمی‌کند؛ باید یک Gem دستی بسازید:

1. مسیر **Explore Gems → New Gem** را باز کنید؛
2. دستور کوتاه ابتدای فایل Workspace Kit را در Instructions قرار دهید؛
3. فایل [`propaymun-ia-workspace-kit.md`](packages/workspace-kit/propaymun-ia-workspace-kit.md) را زیر **Knowledge** اضافه کنید؛
4. Gem را Save کنید.

### استفادهٔ یک‌باره با فایل

اگر یک سرویس فقط فایل را داخل چت می‌پذیرد، Workspace Kit را پیوست و متن کوتاه Workspace Instructions را همراه اولین پیام Paste کنید. این «استفادهٔ موقت از فایل» است؛ نه نصب، نه تنظیم پایدار و نه تضمین فعال‌شدن خودکار.

## محیط‌های دیگرِ Agent Skill

فقط وقتی از بستهٔ Agent Skill استفاده کنید که مستندات خود همان سرویس، فرمت بسته و روش نصب آن را تأیید کرده باشد. این مخزن عمداً دستور نصب CLI تأییدنشده ارائه نمی‌دهد.

## نقشه نصب قابل‌اسکن برای AI

```yaml
product: ProPaymun Information Architecture
skill_id: propaymun-information-architecture
canonical_entrypoint: SKILL.md
native_package: packages/agent-skill/propaymun-information-architecture.zip
native_package_verified_for: [claude.ai-skills]
workspace_knowledge: packages/workspace-kit/propaymun-ia-workspace-kit.md
workspace_instructions: packages/workspace-kit/WORKSPACE_INSTRUCTIONS.md
workspace_requires: [persistent-instructions, file-knowledge]
gemini_web: create-a-new-gem-manually
one_off_file_use: attach-workspace-kit-and-paste-instructions
do_not_claim: [native-installation, persistent-behavior, automatic-triggering, unverified-cli-support]
package_manifest: packages/manifest.json
semantic_schema: schema/semantic-ia.schema.json
companion_schemas: [schema/product-sitemap.schema.json, schema/user-flow.schema.json]
visual_builder_exporter: scripts/export_builder_handoff.py
legacy_download_paths: preserved
release_state: v1.0.1
```

یک AI Installer باید فقط بسته متناسب با محیط را انتخاب کند، محتویات بسته را حفظ کند و آپلود فایل دانش را نصب Native معرفی نکند.

## مهارت چه کاری انجام می‌دهد؟

- قبل از سؤال، بریف، فایل‌ها، گفتگو و منابع مجاز را بررسی می‌کند؛
- در تمام مسیر کفایت اطلاعات را دوباره می‌سنجد و به یک دور سؤال ابتدایی محدود نیست؛
- فقط وقتی پاسخ می‌تواند تصمیم بعدی معماری را تغییر دهد سؤال می‌پرسد و خودش متوقف می‌شود؛
- تشخیص می‌دهد کاربر فعلاً به آشنایی، شکل‌دادن ایده، ساختار پیشنهادی اولیه، IA کامل، ممیزی، سایت‌مپ/یوزرفلوی متمرکز یا تبدیل خروجی نیاز دارد؛
- «نمی‌دانم» را نشانهٔ نیاز به راهنمایی می‌داند: یک شروع برگشت‌پذیر پیشنهاد می‌کند و بدون پرسش‌های زنجیره‌ای ادامه می‌دهد؛
- تصمیم‌های ساختاری را بدون نیاز به دانش تخصصی به پیامدهای کاربر، کسب‌وکار و عملیات تبدیل می‌کند؛
- اجازه نمی‌دهد حافظهٔ میزبان بی‌اجازه Scope، شواهد، نوع خروجی یا زمینهٔ دائمی پروژه را تغییر دهد؛
- با Deltaهای کوتاه، Progressive Disclosure و یک نمایش در هر مرحله مصرف Context را مدیریت می‌کند؛
- زبان را از جغرافیا، قوانین، فرهنگ و مدل عملیاتی جدا می‌کند؛
- پیش از تعیین عمق مدل، تشخیص می‌دهد مسئله Content/Taxonomy، Object/Operation یا Hybrid است؛
- Domainها، Itemهای اصلی، سلسله‌مراتب، روابط، Taxonomy، برچسب‌ها، Metadata، یافت‌پذیری، دسترسی، چرخه عمر و Governance را مدل می‌کند؛
- واقعیت، مشاهده، تأیید، استنباط، پیشنهاد، تعارض و مجهول را مخلوط نمی‌کند؛
- در صورت اثرگذاری و وجود قابلیت، از منابع عمومی جاری استفاده می‌کند؛
- IA پذیرفته‌شده را منبع معنایی خروجی‌های بعدی نگه می‌دارد و اجازه می‌دهد سایت‌مپ محصول یا یوزرفلوی مستقل از یک بستر معنایی حداقلی و نسخه‌دار شروع شود؛
- سایت‌مپ محصول/UX را از XML Sitemap مخصوص SEO تفکیک می‌کند و artifact را بر اساس هدف تصمیم انتخاب می‌کند.

## رفتار تطبیقی

کاربر Mode یا Checkpoint انتخاب نمی‌کند:

```text
بررسی اطلاعات
→ مدل‌سازی لایه بعدی
→ کشف ابهام معماری‌ساز
→ تکمیل تحلیل مستقل و کم‌ریسک
→ پرسیدن کوچک‌ترین سؤال لازم برای همان تصمیم و توقف
→ ادامه پس از پاسخ
→ سنجش آمادگی پیش از ساخت خروجی
```

به‌محض اینکه اطلاعات موجود برای یک مبنای مسئولانه کافی باشد، مهارت به‌جای پرسیدن دربارهٔ هر لایه در یک پیام جدا، یک پاس مفید و منسجم ارائه می‌کند. اگر کاربر پاسخ را نداند، یک نقطهٔ شروع برگشت‌پذیر را با زبان عادی توضیح می‌دهد و پیش از سؤال بعدی یک بخش مفید را جلو می‌برد. کدهای وضعیت داخلی در هندآف ساختاریافته می‌مانند و وارد گفت‌وگوی عادی نمی‌شوند. گزینه‌های دیگر فقط وقتی مطرح می‌شوند که انتخاب را آسان‌تر کنند. زبان یا کلیشهٔ فرهنگی هیچ‌وقت به‌تنهایی قانون محصول نمی‌شود و ثبت‌نام، پرداخت، درآمدزایی یا رشد نیز بدون شواهد یا پذیرش کاربر به تعهد محصول تبدیل نمی‌شوند.

## از IA تا خروجی موردنیاز

IA منبع حقیقت است، نه سقف کار. وقتی معماری برای تصمیم موردنظر به‌اندازهٔ کافی آماده شد، کاربر می‌تواند از آن نمودار، Brief یا تصویر UI، پرامپت پروتوتایپ/ساخت، سایت‌مپ محصول، یوزرفلو، سند/ارائه یا نگاشت فنی بخواهد. مهارت در داخل یک **IA Reference Lock** از ساختار، برچسب‌ها، یافت‌پذیری، دسترسی/حریم خصوصی، شواهد، فرض‌های باز و مرزهای تغییر می‌سازد؛ نام فنی آن فقط وقتی نمایش داده می‌شود که هندآف تیمی یا ماشینی به آن نیاز داشته باشد. سایت‌مپ یا یوزرفلوی مستقل به‌جای اجبار به IA کامل، از یک بستر معنایی حداقلی و نسخه‌دار استفاده می‌کند. اگر محیط فعلی توان تولید مستقیم خروجی را نداشته باشد، یک هندآف خودبسنده و صادقانه تحویل می‌دهد.

## هندآف به ابزارهای سازنده

Figma Make، Lovable و ابزارهای مشابه محیط پایین‌دستی‌اند، نه محل تصمیم‌گیری IA. هر Handoff باید یک هدف روشن داشته باشد: **نمای قابل‌بررسی معماری اطلاعات** یا **نمونهٔ اولیه محصول که به IA متعهد است**.

پس از آماده‌شدن معماری برای هدف موردنظر بنویسید:

```text
از این معماری اطلاعات یک Visual Builder Handoff برای Figma Make بساز.
```

هندآف دو بخش دارد:

1. فایل Markdown خودبسنده شامل مشخصات کامل ساخت؛
2. متن بسیار کوتاه و آماده کپی برای باکس توضیحات ابزار.

این متن کوتاه ضروری است، چون بعضی ابزارها پرامپت بلند را فایل تلقی می‌کنند و تا چیزی در باکس نوشته نشود دکمه Generate فعال نمی‌شود.

خروجی قطعی:

```bash
python scripts/export_builder_handoff.py path/to/ia.json --target figma-make --intent ia-blueprint -o build-spec.md
python scripts/export_builder_handoff.py path/to/ia.json --target lovable --intent product-prototype -o prototype-spec.md
```

در خروجی نمای IA، نمای اول حوزه‌ها، عناصر، سلسله‌مراتب و روابط را نشان می‌دهد. در خروجی نمونهٔ محصول، ابزار سازنده رابط کاربری را بر اساس قیود IA می‌سازد و نقشهٔ داخلی معماری را به‌جای رابط محصول نمایش نمی‌دهد.

## Semantic IA 2.0

قرارداد مستقل از Renderer در [`schema/semantic-ia.schema.json`](schema/semantic-ia.schema.json) قرار دارد و شامل این موارد است:

- اتصال صریح هر Item به Domain؛
- یک فهرست اصلی Itemها؛
- سلسله‌مراتب اصلی و روابط معنادار؛
- نقش‌های مستقل و Permissionهای متصل به Item؛
- وضعیت‌ها و انتقال‌های چرخه عمر؛
- Context محلی همراه با وضعیت شواهد؛
- نوع غالب مسئله و ردگیری نیازهای اطلاعاتی اولویت‌دار؛
- آمادگی هندآف و مجهولات مسدودکننده.

اعتبارسنجی و رندر:

```bash
python scripts/validate_ia_model.py path/to/ia.json
python scripts/render_ia_html.py path/to/ia.json -o ia.html
```

## نقشه مخزن

```text
SKILL.md                     رفتار اصلی
agents/                      Metadata نمایشی Skill
references/                  راهنمای شرطی IA
schema/                      قرارداد Semantic IA 2.0
scripts/                     اعتبارسنجی، رندر، بسته‌بندی و Export
packages/                    بسته‌های حرفه‌ای نصب و راه‌اندازی
install/                     مسیرهای سازگاری برای لینک‌های قبلی
evals/                       سناریوها و معیارهای رفتاری
tests/                       تست‌های قطعی
```

## توسعه و اعتبارسنجی

```bash
python scripts/build_packages.py
python -m unittest discover -s tests -v
python /path/to/skill-creator/scripts/quick_validate.py .
```

GitHub Actions بسته‌ها را بازسازی، برابری بایت‌به‌بایت را بررسی، Fixtureهای مدل معنایی و ماژول‌های جانبی را اعتبارسنجی و تمام تست‌ها را اجرا می‌کند. شواهد بین‌محیطی و معیارهای انتشار در [دروازهٔ انتشار ۱.۰](evals/RELEASE-GATE.md) آمده است.

## نسخه‌بندی و سازگاری

پروژه از Semantic Versioning و [مجوز MIT No Attribution](LICENSE) استفاده می‌کند. نسخهٔ ۱.۰.۰ نخستین قرارداد پایدار است: معماری اطلاعات ۰ تا ۱۰۰ در هسته می‌ماند و سایت‌مپ محصول، یوزرفلوی stateful، راهنمای قابل‌حمل برای محیط‌های فایل‌محور، تبدیل قابل‌ردیابی خروجی و مرزهای اعتبارسنجی مبتنی بر شواهد را همراه خود دارد.

لینک‌های قبلی `install/claude-ai` و `install/universal-web` به‌عنوان Alias سازگار و همگام حفظ می‌شوند؛ مستندات جدید از نام‌های حرفه‌ای بالا استفاده می‌کنند.
