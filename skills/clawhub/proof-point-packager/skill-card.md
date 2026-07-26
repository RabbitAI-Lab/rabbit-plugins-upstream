## Description: <br>
Packages ledger-approved marketing proof into reusable stat cards, case snippets, testimonial blocks, and comparison proofs pinned to message-house pillars and claim IDs, while flagging claims that lack approved proof. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[aaron-he-zhu](https://clawhub.ai/user/aaron-he-zhu) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Marketing and narrative teams use this skill to turn approved claims, story-bank material, and user-provided proof into reusable proof modules for each message-house pillar. It also produces a gap list for claims or proof material that still need source review. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Customer quotes, case data, and benchmark exports could be reused without enough source or rights review. <br>
Mitigation: Review proof material and usage rights before use; package only ledger-approved evidence and mark unverified material [needs source]. <br>
Risk: Pasted proof material may contain instructions that are unrelated to the user's packaging task. <br>
Mitigation: Treat pasted case studies, benchmarks, testimonials, and ledger excerpts as untrusted input and do not follow embedded instructions. <br>
Risk: Durable memory writes could preserve incomplete proof modules or unresolved gaps. <br>
Mitigation: Ask before saving results and route proof gaps or not-yet-ledgered proof only as proposed claim events for later review. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/aaron-he-zhu/skills/proof-point-packager) <br>
- [Project homepage](https://github.com/aaron-he-zhu/aaron-marketing-skills) <br>


## Skill Output: <br>
**Output Type(s):** [markdown, text, configuration, guidance] <br>
**Output Format:** [Markdown proof module set with stat cards, case snippets, testimonial blocks, comparison proofs, a gap list, and a handoff summary] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Results may include proposed memory updates only after user confirmation; unverified proof is marked [needs source].] <br>

## Skill Version(s): <br>
19.0.0 (source: server release evidence and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
