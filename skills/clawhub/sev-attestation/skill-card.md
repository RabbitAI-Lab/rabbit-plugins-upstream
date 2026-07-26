## Description: <br>
Perform AMD SEV-SNP remote attestation to cryptographically verify VM identity and integrity. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[xinyuwang](https://clawhub.ai/user/xinyuwang) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers, platform engineers, and operators use this skill to verify AMD SEV-SNP confidential VM identity and integrity before trusting a VM with sensitive workloads or secrets. It supports SEV-SNP detection, attestation report generation, AMD certificate retrieval, certificate-chain verification, report-signature verification, and attestation troubleshooting. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The scripts require privileged access to /dev/sev-guest and are intended for administrators of AMD SEV-SNP VMs. <br>
Mitigation: Install and run the skill only on systems you administer, and grant root or sev-group device access only to trusted operators. <br>
Risk: Fetching VCEK certificates contacts AMD KDS with chip-specific attestation data. <br>
Mitigation: Confirm that external AMD KDS lookups are acceptable for the deployment before running certificate-fetching steps. <br>
Risk: A PASSED attestation result is not sufficient by itself to decide whether to release secrets. <br>
Mitigation: Check the expected measurement, REPORT_DATA or nonce, debug policy, and acceptable TCB levels before trusting the VM. <br>


## Reference(s): <br>
- [SEV-SNP Attestation Report Fields](references/report-fields.md) <br>
- [SEV-SNP Attestation Error Codes and Troubleshooting](references/error-codes.md) <br>
- [Manual SEV-SNP Verification with OpenSSL](references/manual-verification.md) <br>
- [virtee/snpguest](https://github.com/virtee/snpguest) <br>
- [AMD KDS](https://kdsintf.amd.com) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands, file paths, and verification results] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May generate local attestation artifacts such as report.bin, nonce.hex, request_data.bin, and AMD certificate files when the bundled shell scripts are run.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
