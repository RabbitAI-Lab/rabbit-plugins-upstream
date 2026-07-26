## Description: <br>
Nadname Agent helps agents check and register .nad names on Monad through Nad Name Service, including availability checks, pricing, and registration transactions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[daaab](https://clawhub.ai/user/daaab) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, web3 operators, and agents use this skill to check .nad name availability, estimate costs, register names, and inspect owned names on Monad. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill handles wallet secrets and can submit live blockchain transactions that spend MON tokens. <br>
Mitigation: Use a dedicated low-balance wallet, run registration with --dry-run first, and avoid exposing a primary wallet private key. <br>
Risk: Managed mode stores local wallet material and prints the recovery phrase during setup. <br>
Mitigation: Treat managed mode as experimental, use it only on trusted machines, and store any recovery phrase securely outside shared logs or terminals. <br>
Risk: Some lookup results are simulated or may be overstated as real. <br>
Mitigation: Verify name availability, ownership, pricing, and transaction state through official NNS sources before acting on results. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/daaab/skills/nadname-agent) <br>
- [Nad Name Service app](https://app.nad.domains) <br>
- [Nad Name Service documentation](https://docs.nad.domains) <br>
- [Monad explorer](https://explorer.monad.xyz) <br>
- [Monad bridge](https://bridge.monad.xyz) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with bash command examples and Node.js CLI output.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Commands may perform external API calls and blockchain transactions when executed.] <br>

## Skill Version(s): <br>
2.0.1 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
