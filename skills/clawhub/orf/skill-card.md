## Description: <br>
On-demand ORF news digest in German that selects non-sport ORF headlines, sends each item with title, age, and link, then generates a cartoon ZiB-style studio image based on the selected stories. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[cpojer](https://clawhub.ai/user/cpojer) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and agents use this skill to pull a concise German ORF news digest focused on Austrian and international politics, with sports excluded. It also creates a generated news-studio image that reflects the selected stories. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill reads a Gemini or Nano Banana API key from the environment or local OpenClaw config and sends headline-derived image prompts to an external image service. <br>
Mitigation: Set GEMINI_API_KEY explicitly, review local configuration before use, and avoid adding sensitive information to prompts. <br>
Risk: The image-generation helper installs unpinned Python packages at runtime. <br>
Mitigation: Inspect or pin dependencies and run the skill in an isolated environment before installing or using it. <br>
Risk: The server security review marked the release suspicious because the API-key lookup and runtime package installation are not clearly disclosed. <br>
Mitigation: Review the security summary and scripts before installation, and only run the image-generation step if those behaviors are acceptable. <br>


## Reference(s): <br>
- [ORF News](https://news.orf.at/) <br>
- [ORF RSS Feeds](https://rss.orf.at/) <br>
- [ORF Skill Page](https://clawhub.ai/cpojer/skills/orf) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Files] <br>
**Output Format:** [German 3-line news item messages followed by a generated PNG image.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Defaults to 5 items and caps requests at 15; excludes sports; includes ORF links and relative age text.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
