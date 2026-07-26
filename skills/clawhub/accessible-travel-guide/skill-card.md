## Description: <br>
无障碍出行助手，查询景点、酒店和交通无障碍设施，覆盖轮椅、视障、听障、婴儿车和老年人5类需求，提供热门景区和主流酒店品牌的设施查询与出行建议。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[travel-skills](https://clawhub.ai/user/travel-skills) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and travel-planning agents use this skill to look up accessibility details for supported Chinese attractions and hotel brands, then receive practical travel tips for wheelchair users, visually impaired travelers, hearing impaired travelers, stroller users, and older adults. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill claims local-only operation while evidence.security reports under-explained token and network code. <br>
Mitigation: Review before installation and require the publisher to remove or clearly document PROXY_TOKEN and the outbound request helper before treating the skill as zero-network. <br>
Risk: Accessibility details may be incomplete or outdated because the skill does not provide real-time facility changes. <br>
Mitigation: Confirm critical accessibility details, reservations, and service availability with the venue or hotel before travel. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/travel-skills/skills/accessible-travel-guide) <br>
- [Publisher profile](https://clawhub.ai/user/travel-skills) <br>


## Skill Output: <br>
**Output Type(s):** [Text, JSON, Guidance] <br>
**Output Format:** [JSON strings containing accessibility lookup results or travel guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs are generated from embedded local datasets for supported attractions, hotel brands, accessibility needs, and travel modes.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
