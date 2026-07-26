## Description: <br>
Compress helps agents semantically shorten long text with iterative validation, anchor checksums, and information checks. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent users use this skill to reduce long text into shorter semantic summaries while checking compression quality, anchor integrity, and possible information loss. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Semantic compression can make small meaning changes or lose subtle information. <br>
Mitigation: Review compressed output against the source text, especially when accuracy matters. <br>
Risk: The skill is not appropriate for exact records, credentials, medical instructions, legal terms, financial figures, or safety-critical material. <br>
Mitigation: Do not use it for regulated or safety-critical content; keep authoritative originals when exact wording or values matter. <br>
Risk: The declared exec tool is not clearly needed for ordinary text compression. <br>
Mitigation: Review and approve any proposed command execution before allowing it. <br>


## Reference(s): <br>
- [Compress on ClawHub](https://clawhub.ai/thcjp/skills/compress) <br>
- [Publisher profile: thcjp](https://clawhub.ai/user/thcjp) <br>
- [Clawdis homepage](https://skillhub.cn) <br>


## Skill Output: <br>
**Output Type(s):** [text, json, guidance] <br>
**Output Format:** [Compressed text with JSON quality, validation, and improvement summaries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include anchor checksums, compression scores, loss analysis, and recovery information.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
