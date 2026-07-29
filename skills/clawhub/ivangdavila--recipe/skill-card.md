## Description: <br>
Captures, standardizes, scales, and files recipes into a personal collection that stays searchable and cookable. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ivangdavila](https://clawhub.ai/user/ivangdavila) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users use this skill to capture recipes from links, images, video, dictation, or handwritten cards, then normalize them into a durable personal recipe collection. It also supports recipe scaling, unit conversion, substitutions, equipment rewrites, cost estimates, meal plans, shopping lists, testing notes, and recipe migration. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may retain recipe history, kitchen preferences, allergy or intolerance notes, guest dietary details, and cookbook or catering project notes in local Clawic data folders. <br>
Mitigation: Install it only when durable local recipe assistance is desired, and periodically review or prune the configured Clawic data folders. <br>
Risk: Imported recipe-app exports or sync notes can contain credential-like values. <br>
Mitigation: Store only credential pointers such as environment variable, keychain, or password-manager references, and do not write raw secrets into recipe files. <br>


## Reference(s): <br>
- [ClawHub Recipes skill page](https://clawhub.ai/ivangdavila/skills/recipe) <br>
- [Clawic Recipes homepage](https://clawic.com/skills/recipe) <br>
- [Capture guide](capture.md) <br>
- [Recipe format guide](format.md) <br>
- [Conversion guide](conversion.md) <br>
- [Scaling guide](scaling.md) <br>
- [Substitutions guide](substitutions.md) <br>
- [Planning guide](planning.md) <br>
- [Migration guide](migration.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, configuration, guidance] <br>
**Output Format:** [Markdown recipes, plans, shopping lists, calculations, and local configuration notes] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May create or update local plain-text notes under configured Clawic recipe, health, contacts, and project data folders.] <br>

## Skill Version(s): <br>
1.0.2 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
