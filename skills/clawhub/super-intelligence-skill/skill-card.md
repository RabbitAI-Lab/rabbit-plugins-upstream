## Description:

Gunakan saat user menghadapi task yang butuh reasoning dalam, analisis kompleks, problem-solving kreatif, sintesis long-context, atau planning multi-step. Menyediakan framework kognitif + self-correction loop untuk meningkatkan kualitas output pada task tersebut. Aktif saat user minta 'pikir lebih dalam', 'analisis mendalam', atau 'rencana multi-langkah'.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pmuhammadagus-byte](https://clawhub.ai/user/pmuhammadagus-byte)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users enable this skill for complex analysis, creative problem solving, long-context synthesis, multi-step planning, and requests that need deeper reasoning. The skill provides cognitive frameworks, self-correction loops, context-management patterns, and optional persona guidance that shape how an agent drafts and reviews responses.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can broadly influence agent reasoning, planning, response style, and verbosity across tasks where it is enabled.

Mitigation: Enable it for complex tasks that benefit from deeper analysis, and review the Indonesian instructions and optional SOUL persona guidance before deployment.

Risk: Reasoning frameworks can produce overconfident or overly elaborate guidance if treated as a substitute for policy, factual verification, or user approval.

Mitigation: Keep the artifact guardrails in force: do not override agent safety policy, avoid credential files, confirm major changes, and verify results before claiming success.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/pmuhammadagus-byte/skills/super-intelligence-skill)
- [Reasoning Frameworks](references/reasoning-frameworks.md)
- [Cognitive Patterns from Frontier Models](references/cognitive-patterns.md)
- [Self-Correction & Error Recovery Protocols](references/self-correction.md)
- [Context Management & Long-Context Optimization](references/context-management.md)
- [SOUL Enhancement for Super Intelligence](SOUL_ENHANCEMENT.md)

## Skill Output:

**Output Type(s):** [guidance, markdown, text, configuration]

**Output Format:** [Markdown guidance with structured reasoning protocols and configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [No executable code, declared binaries, credential access, or hidden data handling were identified in server security evidence.]

## Skill Version(s):

1.0.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
