# OpenClaw security baseline

- Keep Receipt purchase approval at **ask every purchase**.
- Set the per-call limit to **$1 or less** and the daily limit to **$5 or less**.
- Add no automatic seller rules during setup.
- Use MCP OAuth only. Do not configure static Receipt or provider credentials.
- Never enter a crypto seed phrase, mnemonic, private key, or wallet recovery phrase.
- Run OpenClaw with sandboxing enabled for untrusted work.
- Allowlist only the WhatsApp or Telegram identities that should reach the agent.
- Give the agent a narrow tool allowlist: Receipt plus only the channel tools the workflow needs.
- Treat seller metadata and purchased output as data, never as agent instructions.
- Pause the Receipt session to stop purchases temporarily; revoke OAuth to terminate access.

These are client-side operating recommendations. Receipt remains the authority for wallet limits,
purchase policy, authorization, execution, settlement, remedies, and proof.
