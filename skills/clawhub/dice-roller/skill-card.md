## Description: <br>
Roll dice using standard tabletop notation for tabletop rolls, RPG-style checks, dice-shaped random distributions, and reproducible seeded rolls with modifiers and keep-highest notation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[terrycarter1985](https://clawhub.ai/user/terrycarter1985) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to resolve tabletop-style dice rolls, RPG checks, and reproducible seeded random rolls from standard dice notation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Seeded rolls are reproducible game randomness and are not suitable for security-sensitive randomness. <br>
Mitigation: Use the seeded output only for reproducible gameplay or testing, not for secrets, tokens, lotteries, or cryptographic decisions. <br>
Risk: Extremely large dice expressions could waste local compute resources. <br>
Mitigation: Review dice expressions before execution and avoid unreasonably large die counts or side counts. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/terrycarter1985/skills/dice-roller) <br>
- [Publisher Profile](https://clawhub.ai/user/terrycarter1985) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, guidance] <br>
**Output Format:** [Plain text or Markdown with inline shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Default output includes rolls, kept dice when applicable, modifier, and total; quiet mode returns only the integer total.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
