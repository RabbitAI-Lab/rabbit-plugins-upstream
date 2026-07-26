## Description: <br>
AI Life Simulator - Experience infinite lives year by year with multiplayer intersections, dynasty mode, challenges, and Moltbook integration. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ezbreadsniper](https://clawhub.ai/user/ezbreadsniper) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External agents and developers use LifePath to run an AI life-simulation game that generates year-by-year narrative lives, supports Telegram play, and can share completed stories to Moltbook. The skill also includes server code, database setup, and integrations for image generation, challenges, dynasty play, and donations or premium access. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The security evidence reports exposed Gemini API keys and weakly scoped deployment controls. <br>
Mitigation: Remove embedded keys, rotate any exposed credentials, and load secrets from a managed environment or secret store before installation or deployment. <br>
Risk: The security evidence warns that database setup and user-data handling need stronger controls. <br>
Mitigation: Use a unique least-privilege PostgreSQL user with a strong password, and review database access paths before storing user profiles or life stories. <br>
Risk: The security evidence says life stories and profile attributes may be sent to Gemini, Banana.dev, Telegram, Moltbook, and donation or payment integrations. <br>
Mitigation: Keep the server private until authentication, authorization, sharing consent, and data-flow review are complete. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ezbreadsniper/skills/lifepath) <br>
- [Project homepage declared by artifact](https://github.com/sehil-systems/lifepath) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, API responses, Images] <br>
**Output Format:** [Markdown documentation, shell commands, JavaScript server code, JSON API responses, generated narrative text, and optional PNG image files.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires Node.js, PostgreSQL, GEMINI_API_KEY, and DATABASE_URL; optional integrations use Telegram, Banana.dev, Moltbook, and payment or donation configuration.] <br>

## Skill Version(s): <br>
2.0.0 (source: SKILL.md frontmatter and server release metadata; package.json reports 1.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
