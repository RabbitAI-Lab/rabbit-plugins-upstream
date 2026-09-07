---
name: telegram-persian-enforcer
description: Enforce Persian output for all Telegram group, channel, and DM interactions.
version: 1.0.0
metadata:
  openclaw:
    requires:
      env: []
      bins: []
    primaryEnv: ""
    emoji: "🇮🇷"
    models: []
---

# Telegram Persian Enforcer

Enforces Persian (Farsi) language output for all Telegram interactions.

## When to Use

Activate when working with Telegram groups, channels, or direct messages where Persian-language output is required. Applies to:
- Chat responses
- Automation output
- Reports and summaries
- Job execution results

## Rules

1. **All generated text must be in Persian (Farsi).**
2. **All reports, summaries, and job-related outputs intended for Telegram must be translated to or drafted in Persian.**
3. **If receiving input in another language, acknowledge it (if needed) but respond exclusively in Persian.**

## Behavior Guidelines

- If the user provides input in English, Persian, or any other language — your Telegram-facing output is always Persian.
- Do not mix languages in Telegram output unless specifically requested by the user within the conversation.
- For code blocks, technical terms, and URLs: keep them in their original language (code is universal), but wrap explanations in Persian.
- Never output English (or any other language) as the primary language in Telegram channels/groups/DMs.

## Example

User asks: "Summarize this article about AI regulation."

Agent response (for Telegram):

```
خلاصه مقاله درباره مقررات هوش مصنوعی:

- قوانین جدید بر شفافیت الگوریتم‌ها تمرکز دارد
- شرکت‌ها موظف به ارائه گزارش‌های سالانه هستند
- جریمه‌های مالی تا ۴٪ درآمد سالانه پیش‌بینی شده است
```

## Limitations

- This skill does not translate incoming messages — it only enforces outgoing Persian output.
- Code snippets, commands, and technical strings retain their original language.
- Does not apply to non-Telegram contexts (e.g., terminal output, file generation) unless explicitly combined with another skill.

---

# تلگرام پارسijan enforcement

تضمین می‌کند که تمام خروجی‌های تلگرام به زبان فارسی تولید شوند — پاسخ‌ها، گزارش‌ها، خلاصه‌ها و متن‌های مربوط به وظایف برای گروه‌ها، کانال‌ها و پیام‌های مستقیم.

## زمان استفاده

هنگام کار با گروه‌ها، کانال‌ها یا پیام‌های مستقیم تلگرام که نیاز به خروجی فارسی دارند فعال می‌شود. شامل:
- پاسخ‌های چت
- خروجی‌های خودکار
- گزارش‌ها و خلاصه‌ها
- نتایج اجرای وظایف

## قوانین

1. **تمام متن تولید شده باید به زبان فارسی باشد.**
2. **تمام گزارش‌ها، خلاصه‌ها و خروجی‌های کاری که برای تلگرام intended هستند باید به فارسی ترجمه یا نوشته شوند.**
3. **دریافت ورودی به زبان دیگر، اگر لازم است تأیید شود اما فقط به فارسی پاسخ داده شود.**

## راهنمای رفتار

- اگر کاربر ورودی را به انگلیسی، فارسی یا هر زبان دیگری ارائه دهد — خروجی شما در تلگرام همیشه فارسی است.
- مگر اینکه کاربر به طور خاص درخواست کند، زبان‌ها را در خروجی تلگرام ترکیب نکنید.
- برای بلوک‌های کد، اصطلاحات فنی و URLها: آن‌ها را به زبان اصلی نگه دارید (کد جهانی است)، اما توضیحات را به فارسی بنویسید.
- هرگز در کانال‌ها/گروه‌ها/پیام‌های مستقیم تلگرام به زبان اصلی (انگلیسی یا غیره) خروجی ندهید.

## مثال

کاربر می‌پرسد: "این مقاله درباره مقررات هوش مصنوعی را خلاصه کن."

پاسخ عامل (برای تلگرام):

```
خلاصه مقاله درباره مقررات هوش مصنوعی:

- قوانین جدید بر شفافیت الگوریتم‌ها تمرکز دارد
- شرکت‌ها موظف به ارائه گزارش‌های سالانه هستند
- جریمه‌های مالی تا ۴٪ درآمد سالانه پیش‌بینی شده است
```

## محدودیت‌ها

- این skill پیام‌های ورودی را ترجمه نمی‌کند — فقط خروجی فارسی را强制执行 می‌کند.
- قطعات کد، دستورات و رشته‌های فنی زبان اصلی خود را حفظ می‌کنند.
- به زمینه‌های غیرتلگرامی (مثلاُاً خروجی ترمينال، توليد فایل) اعمال نمي‌شود مگر اينکه به طور صريح با skill ديگري تركيب شود.
