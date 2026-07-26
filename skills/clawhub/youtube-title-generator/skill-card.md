## Description: <br>
Generates compelling YouTube title ideas from content concepts. Use when someone needs click-worthy video titles using proven structural formulas and psychological patterns from high-performing videos. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[vincentchan](https://clawhub.ai/user/vincentchan) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Creators, marketers, and agents use this skill to turn content ideas, articles, newsletters, or reference material into 30 YouTube title candidates with a brief analysis of the title patterns used. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: User-provided URLs may contain internal, credential-bearing, private-network, or sensitive content that the agent would fetch and analyze. <br>
Mitigation: Provide only URLs that are appropriate for the runtime to access, and avoid sensitive URLs unless the runtime's fetch protections and trust boundary are acceptable. <br>
Risk: Generated title files may preserve details from the user's source material in the local youtube-title/ directory. <br>
Mitigation: Review generated Markdown files before sharing, publishing, or committing them. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/vincentchan/skills/youtube-title-generator) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Markdown file with numbered title lists and analysis] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces 30 distinct title ideas, grouped as 20 structured titles and 10 creative titles, and saves them to a timestamped file under youtube-title/.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
