## Description: <br>
Assesses public healthcare-AI vendor documents to identify gaps between AI use claims, legal language, and HIPAA rules on PHI handling and model training. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dangsllc](https://clawhub.ai/user/dangsllc) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Compliance reviewers, legal teams, and healthcare vendor reviewers use this skill to triage public product pages, Terms of Service, and Privacy Policy materials for documentation gaps about AI use, PHI handling, model improvement, and HIPAA requirements. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The assessment can be mistaken for legal advice or proof of actual PHI handling. <br>
Mitigation: Treat results as public-document compliance triage and have a qualified reviewer validate any gap analysis before vendor decisions. <br>
Risk: Supplying non-public or sensitive documents could broaden the review beyond the intended public-document scope. <br>
Mitigation: Provide only documents the user intends the agent to read, preferably public product, Terms of Service, and Privacy Policy materials. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/dangsllc/skills/ai-claims-assessment) <br>
- [Rote Compliance Skills](https://github.com/Rote-Compliance/rote-compliance-skills) <br>
- [Rote Compliance](https://rotecompliance.com) <br>
- [Dang's Solutions](https://dangssolutions.com) <br>


## Skill Output: <br>
**Output Type(s):** [Analysis, JSON, Guidance] <br>
**Output Format:** [JSON object with cited gap records and a target-level gap summary] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Read-only public-document assessment; cites supplied vendor documents and included HIPAA reference text.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
