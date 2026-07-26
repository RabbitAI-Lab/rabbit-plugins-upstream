## Description: <br>
Analyzes authorized child bedroom night audio/video for crying, fear-of-dark behavior, nightmare wakeups, and out-of-bed events, then returns structured soothing actions and report links. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[18072937735](https://clawhub.ai/user/18072937735) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users or developers use this skill to analyze authorized child bedroom or nursery night recordings and review detected unrest events, suggested soothing actions, and report history. It is intended for behavior detection and caregiver support, not medical diagnosis. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Highly sensitive child bedroom audio/video may be uploaded to or referenced by remote services. <br>
Mitigation: Use only with trusted publisher and backend services, confirmed caregiver authorization, and an understood retention and report-access model. <br>
Risk: The skill may create or reuse local and remote identities and link cloud report history automatically. <br>
Mitigation: Review identity and token storage before deployment, run in a controlled environment, and clear local identity state between users or households. <br>
Risk: Behavior detection and soothing recommendations could be mistaken for medical or psychological diagnosis. <br>
Mitigation: Treat outputs as caregiver support only; repeated or severe sleep events should be referred to appropriate pediatric sleep or child psychology professionals. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/18072937735/skills/smyx-child-bedtime-soothing-analysis) <br>
- [API Interface Documentation](references/api_doc.md) <br>
- [Skill Demo](https://lifeemergence.com/sample.html) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, shell commands, guidance] <br>
**Output Format:** [Markdown text with structured analysis results, soothing recommendations, and report links; JSON output is available for detailed results.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Can save results to a file with --output; history queries are retrieved from the remote report service.] <br>

## Skill Version(s): <br>
1.0.5 (source: SKILL.md frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
