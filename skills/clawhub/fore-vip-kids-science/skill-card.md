## Description:

Children's popular-science Q&A skill that answers kids' curiosity questions with accurate, age-appropriate explanations, generates one child-safe ImageGen illustration per answer section, and outputs a typeset picture-book HTML page.

This skill is ready for commercial/non-commercial use.

## Publisher:

[onsoul](https://clawhub.ai/user/onsoul)

### License/Terms of Use:

MIT-0

## Use Case:

Parents, educators, and children use this skill to turn children's science questions into age-appropriate illustrated explanations. It is intended for child-safe science topics such as nature, animals, space, technology, and everyday phenomena.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Illustrated pages may include a child's name, school, location, health details, or other personal information.

Mitigation: Use local-only output for prompts or generated pages containing children's personal information.

Risk: Sharing to the content library, IMA, or Tencent Docs can publish the final HTML page to an external service.

Mitigation: Confirm the user is comfortable publishing the final HTML page before selecting any remote sharing option.

Risk: Children's science answers or illustrations could become inappropriate when prompts ask for unsafe experiments, medical advice, frightening content, or adult topics.

Mitigation: Apply the skill's age and safety guide, avoid dangerous instructions and medical guidance, and rewrite or decline unsafe child-facing content.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/onsoul/skills/fore-vip-kids-science)
- [Fore.vip](https://fore.vip)
- [ImageGen Per-Section Illustration Guide](references/image-gen-guide.md)
- [Safety and Age Guide](references/safety-and-age-guide.md)
- [HTML Layout Guide](references/layout-guide.md)
- [Sharing Guide](references/share-guide.md)
- [IMA Connection Guide](references/ima-connect-guide.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Files, Guidance]

**Output Format:** [Markdown response with generated images and a self-contained HTML page file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generates one child-safe illustration per answer section when ImageGen is available; falls back to text-only output if image generation is unavailable.]

## Skill Version(s):

1.0.0 (source: server release metadata; artifact frontmatter reports 1.3.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
