## Description: <br>
This skill enables IP address masking and accessing hidden services on the Anyone Network by routing requests through a local SOCKS5 proxy. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ra3ka](https://clawhub.ai/user/ra3ka) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agents use this skill to set up and route selected requests through the Anyone Protocol network for IP masking and access to hidden services. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Selected traffic is routed through the Anyone Network, which may be inappropriate for secrets, regulated data, or internal data under some policies. <br>
Mitigation: Only proxy traffic intentionally approved for this route and avoid secrets or regulated/internal data unless policy allows it. <br>
Risk: The setup uses a global npm install and npx execution of a third-party package. <br>
Mitigation: Verify the npm package and publisher before installation or execution. <br>
Risk: The proxy can persist across requests once started. <br>
Mitigation: Stop the proxy when finished. <br>


## Reference(s): <br>
- [Anyone Network](https://anyone.io) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, code, configuration] <br>
**Output Format:** [Markdown with inline bash and JavaScript code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses a local SOCKS5 proxy on port 9050 by default; initial circuit setup may take up to 30 seconds.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
