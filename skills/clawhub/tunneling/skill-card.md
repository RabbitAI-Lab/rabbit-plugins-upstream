## Description: <br>
Create free SSH tunnels to expose local ports to the internet using tinyfi.sh. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[simantak-dabhade](https://clawhub.ai/user/simantak-dabhade) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and engineers use this skill to create public HTTPS URLs for locally running services when sharing apps, testing webhooks, or demoing prototypes. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Exposing a local port can make private, admin, debug, or unauthenticated services reachable from the public internet. <br>
Mitigation: Confirm the exact port before use, avoid sensitive interfaces, prefer services with their own authentication, and stop the SSH process when the tunnel is no longer needed. <br>
Risk: Long-running tunnels can keep a local service publicly reachable longer than intended. <br>
Mitigation: Use keep-alive only when stability is needed, monitor active SSH sessions, and close tunnels after demos, webhook tests, or sharing sessions are complete. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/simantak-dabhade/skills/tunneling) <br>
- [TinyFish tunneling service](https://tinyfi.sh) <br>


## Skill Output: <br>
**Output Type(s):** [shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline bash commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes local port selection, optional subdomain selection, keep-alive settings, and the resulting public tunnel URL.] <br>

## Skill Version(s): <br>
1.0.0 (source: release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
