## Description: <br>
Essential curl commands for HTTP requests, API testing, and file transfers. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dreamboat2000](https://clawhub.ai/user/dreamboat2000) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, API testers, and engineers use this skill as a concise curl command reference for HTTP requests, authentication, debugging, file transfers, and response handling. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Credentials, API keys, cookies, and trace files used in curl examples can expose sensitive data if stored in shell history or local files. <br>
Mitigation: Use environment variables or secure secret handling instead of inline secrets, treat cookie and trace files as sensitive, and delete temporary files when finished. <br>
Risk: Downloaded files may be unsafe or unsuitable to open or share without inspection. <br>
Mitigation: Inspect downloaded files before opening or redistributing them. <br>
Risk: Skipping TLS certificate validation with curl can hide connection security problems. <br>
Mitigation: Use insecure TLS options only for controlled troubleshooting and avoid them in production workflows. <br>


## Reference(s): <br>
- [Curl Http on ClawHub](https://clawhub.ai/dreamboat2000/curl-http) <br>
- [curl homepage](https://curl.se/) <br>
- [curl documentation](https://curl.se/docs/) <br>
- [MDN HTTP request methods](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods) <br>


## Skill Output: <br>
**Output Type(s):** [markdown, shell commands, code, guidance] <br>
**Output Format:** [Markdown with bash command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires curl; examples may also use jq for JSON formatting.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
