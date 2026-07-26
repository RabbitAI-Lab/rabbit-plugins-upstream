## Description: <br>
Scans nearby BLE MAC addresses, hashes them with a salt, and records local proof nodes for soulbound $ANIMA token minting. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[penguinx01](https://clawhub.ai/user/penguinx01) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and technically capable users use this skill to run a local BLE scan, derive hashed proofs from nearby device identifiers, and store the resulting proof graph locally. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: BLE scanning can expose or correlate nearby device identifiers. <br>
Mitigation: Run the scan only when intentionally authorized, and treat terminal output plus anima_dag.gpickle as sensitive. <br>
Risk: Unpinned Python dependencies can change behavior across installs. <br>
Mitigation: Pin dependency versions before installation when using the skill in a controlled environment. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/penguinx01/skills/ble-anima-minter) <br>
- [ClawHub publisher profile](https://clawhub.ai/user/penguinx01) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands] <br>
**Output Format:** [Markdown with inline bash code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [When run, the included script prints detected device identifiers and hashes, then writes a local anima_dag.gpickle proof file.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
