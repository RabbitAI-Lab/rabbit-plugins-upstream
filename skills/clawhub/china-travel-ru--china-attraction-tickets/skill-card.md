## Description: <br>
Откройте для себя лучшие достопримечательности Китая с ценами на билеты, часами работы и ссылками для бронирования через Trip.com; также поддерживаются отели, авиабилеты, планирование поездки и советы для путешественников. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[china-travel-ru](https://clawhub.ai/user/china-travel-ru) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External travelers and travel-planning agents use this skill to find China attraction tickets, opening hours, booking links, hotel and flight options, itineraries, and practical travel advice in Russian. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: User travel-planning queries are sent to an external proxy endpoint. <br>
Mitigation: Install only if that data flow is acceptable, avoid entering sensitive personal details, and review the backend and privacy policy before use. <br>
Risk: The artifact embeds a reusable proxy token. <br>
Mitigation: Prefer a release that removes the bundled token and uses user-provided environment variables or per-user credentials. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/china-travel-ru/skills/china-attraction-tickets) <br>
- [Publisher profile](https://clawhub.ai/user/china-travel-ru) <br>
- [External proxy endpoint listed in evidence](https://1439498936-eu423jdjnd.ap-guangzhou.tencentscf.com) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, Shell commands, Guidance] <br>
**Output Format:** [Markdown travel recommendations with inline shell command examples and JSON status from the helper script] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs may include attraction ticket prices, opening hours, booking links, hotel and flight options, itineraries, and travel tips returned through an external proxy.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
