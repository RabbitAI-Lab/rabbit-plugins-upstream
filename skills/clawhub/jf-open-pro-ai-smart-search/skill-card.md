## Description:

JF Tech Pro AI Smart Search helps agents search JF cloud-stored alarm videos with semantic queries such as a person with a hat, car, or dog, then return matching clips and playback information.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jftech](https://clawhub.ai/user/jftech)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and operators use this skill to search JF Tech cloud alarm footage by natural-language event descriptions and retrieve matching video segments or playback URLs. It supports workflows for semantic video lookup, AI event search, and cloud-storage playback review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can query cloud-stored alarm footage and generate direct playback or download URLs for surveillance video.

Mitigation: Install it only for intended JF Tech video-search workflows, restrict access to authorized operators, and treat printed playback URLs as sensitive data.

Risk: Credentials and device identifiers control access to video search and playback APIs.

Mitigation: Use least-privilege JF credentials, provide them only through environment variables, and rotate them if logs or terminal output may have exposed them.

Risk: Changing the API endpoint could send requests outside the expected JF Tech service boundary.

Mitigation: Keep JF_ENDPOINT limited to official JF hosts such as api.jftechws.com or api-cn.jftech.com.

## Reference(s):

- [JF Tech API Reference](references/jftech-api.md)
- [AI Search Query Examples](references/search-examples.md)
- [JF Open Platform](https://open.jftech.com/)
- [JF Tech Developer Platform](https://developer.jftech.com)
- [JF Tech API Documentation](https://docs.jftech.com/)
- [JF Tech AI Smart Search Documentation](https://docs.jftech.com/docs?menusId=54582398fd8d4248962354e92ac2e47a&siderId=d2c0d9105d9c4b78bc0d2ee3851d2557)
- [JF Tech Cloud Playback API Documentation](https://docs.jftech.com/docs?menusId=54582398fd8d4248962354e92ac2e47a&siderId=2e08468f46564602d01ae8a244661672)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration instructions, API Calls]

**Output Format:** [Markdown guidance with Python command examples and optional JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires JF credentials and device identifiers from environment variables; generated playback URLs should be treated as sensitive.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
