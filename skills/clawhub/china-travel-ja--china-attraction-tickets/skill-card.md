## Description: <br>
中国のトップ観光スポットをチケット料金、営業時間、Trip.com予約リンクで発見します。ホテル、フライト、旅行計画、旅行アドバイスもサポート。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[china-travel-ja](https://clawhub.ai/user/china-travel-ja) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External travelers and travel planners use this skill to find China attraction tickets, opening hours, booking links, hotels, flights, itineraries, and travel advice in Japanese. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill sends travel plans and questions to a fixed Tencent SCF proxy and onward to TripGenie. <br>
Mitigation: Confirm users are comfortable with this data flow before installation and ask the publisher to clarify endpoint ownership, logging, and retention. <br>
Risk: The artifact embeds a proxy token while also declaring PROXY_URL and PROXY_TOKEN environment variables. <br>
Mitigation: Remove or rotate embedded credentials and use environment variables or server-side credential injection consistently before production use. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/china-travel-ja/skills/china-attraction-tickets) <br>
- [Publisher profile](https://clawhub.ai/user/china-travel-ja) <br>
- [Tencent SCF proxy endpoint](https://1439498936-eu423jdjnd.ap-guangzhou.tencentscf.com) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Guidance] <br>
**Output Format:** [Markdown travel results and JSON command output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Results may include attraction details, ticket prices, opening hours, Trip.com booking links, hotel and flight options, itineraries, and travel tips.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
