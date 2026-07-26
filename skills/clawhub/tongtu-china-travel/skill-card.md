## Description: <br>
Plan trips to China with flight, hotel, train, and attraction search, plus visa, payment, transport, eSIM, and city-guide assistance in English, Korean, Japanese, and other languages. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jesse-tzx](https://clawhub.ai/user/jesse-tzx) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External travelers and travel-planning agents use this skill to plan trips to China, compare flights, hotels, trains, and attractions, and get practical guidance on visas, payment, communications, and local transport. The skill is intended to answer in the user's language and present booking guidance without exposing raw booking URLs. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill depends on the external flyai CLI from npm and may send travel search details such as cities, dates, and preferences to that service. <br>
Mitigation: Install only after accepting that dependency and avoid entering sensitive personal details unless they are required for the travel query. <br>
Risk: Visa, payment, transport, and booking information can affect real travel decisions and may become outdated. <br>
Mitigation: Treat the output as travel assistance and verify critical details with official providers before purchasing or traveling. <br>
Risk: Raw booking URLs from flyai or affiliated booking services could expose users to opaque booking flows. <br>
Mitigation: Follow the artifact behavior that removes raw booking URLs from user-facing output and directs users to search within Alipay AliTrip or official alternatives. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/jesse-tzx/skills/tongtu-china-travel) <br>
- [Server-resolved GitHub provenance](https://github.com/jesse-tzx/tongtu-china-travel/tree/main/skills/tongtu-china-travel) <br>
- [Source repository homepage](https://github.com/jesse-tzx/tongtu-china-travel) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Markdown with tables, lists, images, booking guidance, and occasional inline shell commands.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Responds in the user's detected language, translates China travel search parameters to Chinese for flyai commands, keeps results concise, and removes raw flyai booking URLs from user-facing output.] <br>

## Skill Version(s): <br>
0.3.8 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
