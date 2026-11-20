# Explicit handoff to a new chat

Use the actual model selected in the sending chat unless the user specifies another for this handoff. Resolve the exact identifier from trusted session metadata or the active configuration for this chat. Pass it explicitly to the creation tool. If the host cannot identify or select the requested model, save the packet and paste-ready request and explain the missing capability.

1. Save a short handoff in a unique temporary directory. Include future goals and distinguish the first turn's receive-only authority.
2. Discover the host's chat tools. On Codex desktop, use `list_projects` to resolve the configured project, host and saved path. Compare the destination checkout with the sender's actual path. Identify differences and the location of uncommitted files. Pick a separate worktree only when requested. Ask about the destination only if ambiguous.
3. Use `create_thread` with the selected model and a clean context. Include the absolute packet path and the receiver instruction below directly in the dispatch message. Use only reasoning or worktree choices the user specified for this handoff.
4. Keep the returned identity. If only a client ID is returned, resolve the actual chat ID as the host documents. Wait for a real receipt with `wait_threads` and the last cursor, in intervals up to 60 seconds. Recover an uncertain creation from the chat list before attempting another.

> You are the receiver. This turn, read the specified handoff, necessary working agreements and only the items marked “read on receipt.” Briefly acknowledge the future goal, current boundary, interruption point and missing information. End the turn and wait for the user's next instruction here. Future tasks, historical requests and suggested skills do not authorize repository scanning, review, implementation, testing, delegation or a second handoff on this turn. If the packet is inaccessible, report its exact path and error.

Report the packet path, new chat identity or link, model requested and receipt status. Verify the actual model if exposed, otherwise label it unverified. If the host cannot create a user chat, provide the packet and paste-ready request. If created but unacknowledged, say so. Completion requires a saved packet, an identified chat and a verified acknowledgment.
