## Description:

Создаёт проверенное по открытым источникам досье на живого человека перед деловой встречей, выдавая текст по-русски в чате и документ Word.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sergeypetrakov](https://clawhub.ai/user/sergeypetrakov)

### License/Terms of Use:

MIT-0

## Use Case:

Пользователи готовятся к деловым встречам и переговорам: собирают подтверждённые сведения о конкретном человеке, его публичной деятельности и возможных темах разговора.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Составление досье на живых людей может привести к вторжению в частную жизнь или злоупотреблениям.

Mitigation: Использовать только для законной подготовки к встрече; не исследовать частных лиц и не применять для преследования, дискриминации или сбора чувствительных личных сведений.

Risk: Поисковые запросы и проверяемые факты передаются Perplexity, а журналы запросов и кэш остаются локально.

Mitigation: Не отправлять конфиденциальные сведения; ограничить доступ к рабочим файлам и удалять журналы и кэш по окончании работы.

Risk: Проверка источников загружает внешние URL без строгого ограничения сетевых адресов.

Mitigation: Запускать в среде, где исходящие запросы не могут достигать внутренних сервисов.

## Reference(s):

- [Страница навыка в ClawHub](https://clawhub.ai/sergeypetrakov/skills/dossier)
- [Справочник по поиску](references/search-playbook.md)

## Skill Output:

**Output Type(s):** [Text, Files]

**Output Format:** [Русский текст в чате и документ Word (.docx)]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Досье со ссылками на источники; обычно две страницы, до трёх при наличии контекста встречи.]

## Skill Version(s):

1.0.6 (source: frontmatter and server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
