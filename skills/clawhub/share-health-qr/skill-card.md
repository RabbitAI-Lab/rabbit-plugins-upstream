## Description: <br>
Generates a patient-controlled SMART Health Link (SHL) QR code that lets a patient share selected health records with a clinic or provider without direct-encoding PHI in the QR image. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[aks129](https://clawhub.ai/user/aks129) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Patients and healthcare-facing agents use this skill to generate consented SMART Health Link QR codes for clinic check-in or provider record sharing. It guides the agent through confirming scope, expiry, and label, generating the SHL, delivering the viewer link, and keeping the revocation manage link private to the patient. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: A QR code could become an irreversible PHI copy if health data is encoded directly. <br>
Mitigation: Encode only the SHL server's encrypted shlink:/ pointer and stop if a real SHL cannot be generated. <br>
Risk: Patients may share more records, for longer, or under a more revealing label than intended. <br>
Mitigation: Confirm the profile, expiry, and visible label with the patient before each QR generation. <br>
Risk: Viewer and manage links can expose access paths or revocation authority if sent to the wrong party. <br>
Mitigation: Treat both links as sensitive and deliver the manage link only in a private message or distinct patient-only section. <br>
Risk: Using the skill outside a configured SHL/FHIR workflow can create misleading or nonfunctional sharing flows. <br>
Mitigation: Install it only where SHL_SERVER_URL and STEP_UP_SECRET are configured and surface simulation responses without improvising a replacement QR. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/aks129/skills/share-health-qr) <br>
- [Publisher profile](https://clawhub.ai/user/aks129) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with inline tool-call examples, QR delivery steps, and setup shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs should encode only the returned shlink:/ URI in the QR and keep viewer and manage links separate.] <br>

## Skill Version(s): <br>
1.6.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
