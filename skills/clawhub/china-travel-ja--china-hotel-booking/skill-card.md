## Description: <br>
中国のホテルを検索し、リアルタイムのおすすめ、料金、予約リンクを提供します。チェックイン・チェックアウト日、人数、予算、位置の希望で絞り込み可能。北京、上海、西安、成都など人気旅行先をカバーし、Trip.com direct予約に対応。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[china-travel-ja](https://clawhub.ai/user/china-travel-ja) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External travelers and travel-planning agents use this skill to find and compare hotels in Chinese cities by date, guest count, budget, and location preferences. It returns hotel recommendations with pricing, ratings, key features, and booking links in Japanese. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill sends travel plans, preferences, dates, guest counts, and free-form queries to a remote proxy. <br>
Mitigation: Avoid entering sensitive personal details unless the user is comfortable sharing them with the backend service. <br>
Risk: The implementation exposes broader travel and free-form query behavior than the hotel-focused listing describes. <br>
Mitigation: Review outputs for scope fit before relying on non-hotel travel advice or booking recommendations. <br>


## Reference(s): <br>
- [ClawHub Skill Listing](https://clawhub.ai/china-travel-ja/skills/china-hotel-booking) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, JSON, Shell commands, Guidance] <br>
**Output Format:** [JSON response containing Markdown travel and hotel recommendations] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs may include hotel names, prices, ratings, key features, booking links, and related travel guidance.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
