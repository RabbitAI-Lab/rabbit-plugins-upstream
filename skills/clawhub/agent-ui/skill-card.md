## Description: <br>
Batteries-included agent component for React/Next.js from ui.inference.sh, with runtime, tools, streaming, approvals, widgets, client-side tools, and form-filling support. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[okaris](https://clawhub.ai/user/okaris) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers use this skill to add an agent UI to React or Next.js applications for AI chat interfaces, SaaS copilots, assistants, human approval flows, streaming responses, widgets, and browser-side tools. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill instructs users to install a remote shadcn component and the @inferencesh/sdk package, which creates normal third-party dependency risk. <br>
Mitigation: Review the remote component and SDK package before installation, and pin versions where practical. <br>
Risk: The setup uses INFERENCE_API_KEY and a proxy route that could expose secrets or allow unintended access if configured carelessly. <br>
Mitigation: Keep INFERENCE_API_KEY server-side only, protect the proxy route with authentication and rate limits, and avoid logging secrets or sensitive prompts or files. <br>
Risk: Browser-side tools may take actions in the user's interface. <br>
Mitigation: Restrict client-side tools to actions users explicitly approve. <br>


## Reference(s): <br>
- [Agent Component Docs](https://ui.inference.sh/blocks/agent) <br>
- [Agents Overview](https://inference.sh/docs/agents/overview) <br>
- [Agent SDK](https://inference.sh/docs/api/agent/overview) <br>
- [Human-in-the-Loop](https://inference.sh/docs/runtime/human-in-the-loop) <br>
- [Agents That Generate UI](https://inference.sh/blog/ux/generative-ui) <br>
- [Agent UX Patterns](https://inference.sh/blog/ux/agent-ux-patterns) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Code, Configuration] <br>
**Output Format:** [Markdown with bash, TypeScript, and TSX code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes component installation, SDK setup, proxy route configuration, environment variable guidance, React usage examples, prop descriptions, and related skill commands.] <br>

## Skill Version(s): <br>
0.1.5 (source: server evidence release.version) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
