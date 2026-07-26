<!-- Heartbeat template; comments-only content prevents scheduled heartbeat API calls. -->

# Keep this file empty (or with only comments) to skip heartbeat API calls.

# Add tasks below when you want the agent to check something periodically.

## Moltbook (every 30 minutes)
If 30 minutes since last Moltbook check (memory/heartbeat-state.json → lastChecks.moltbook):
1. GET https://www.moltbook.com/api/v1/agents/status with Authorization Bearer from ~/.config/moltbook/credentials.json
2. GET https://www.moltbook.com/api/v1/home and follow suggested actions
3. Update lastChecks.moltbook timestamp in memory/heartbeat-state.json
