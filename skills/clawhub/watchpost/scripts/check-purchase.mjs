#!/usr/bin/env node
// Watchpost purchase check for open agents (OpenClaw / Hermes / any agentskills
// runtime). Calls the hosted Watchpost verdict API with the user's connection
// token and prints the verdict. The exit code encodes the decision so the agent
// can gate on it: 0 = approve, 2 = review (ask the user), 1 = block or error.
//
// Usage:
//   node check-purchase.mjs '{"merchant":"amazon.com","title":"USB-C cable","amountMinor":1599,"currency":"USD","isRecurring":false}'
// Env: WATCHPOST_TOKEN (required) — the user's own Watchpost connection token.
//
// Security note: this script reads exactly one env var (the user's own Watchpost
// token) and sends it, in an Authorization header, to a single HARDCODED endpoint
// (Watchpost's official API, below). The destination is not configurable, so the
// token can never be redirected anywhere else. No other environment variables are
// read. Source is MIT-0 and fully auditable.

const raw = process.argv[2];
if (!raw) {
	console.error(
		'Pass the purchase as a JSON argument, e.g. \'{"merchant":"amazon.com","title":"...","amountMinor":1599,"currency":"USD"}\'',
	);
	process.exit(3);
}

let purchase;
try {
	purchase = JSON.parse(raw);
} catch {
	console.error("The argument must be valid JSON.");
	process.exit(3);
}

// The user's own Watchpost connection token (wp_…). Sent only to the official
// endpoint below, in the Authorization header, to authenticate this one check.
const token = process.env.WATCHPOST_TOKEN;
if (!token) {
	console.error(
		"Set WATCHPOST_TOKEN to the user's Watchpost connection token (wp_…).\n" +
			"Get one at https://app.watchpost.systems/connections?ref=clawhub — free account, no card.",
	);
	process.exit(3);
}

if (!purchase.merchant || !purchase.title || !Number.isFinite(purchase.amountMinor)) {
	console.error("Need at least merchant, title, and a numeric amountMinor (cents).");
	process.exit(3);
}

// Fixed, official endpoint — hardcoded (NOT read from the environment) so the
// connection token can only ever be sent to Watchpost's own API, never to any
// other host. This is the only network destination in this script.
const base = "https://api.watchpost.systems";

const body = {
	agent: { name: "openclaw", runtime: "agentskills" },
	merchant: { domain: String(purchase.merchant) },
	product: {
		title: String(purchase.title),
		url: purchase.url,
		description: purchase.description,
	},
	payment: {
		amountMinor: Math.round(purchase.amountMinor),
		currency: (purchase.currency || "USD").toUpperCase(),
		isRecurring: Boolean(purchase.isRecurring),
	},
};

let res;
try {
	res = await fetch(`${base}/v1/verify`, {
		method: "POST",
		headers: { "content-type": "application/json", authorization: `Bearer ${token}` },
		body: JSON.stringify(body),
	});
} catch (e) {
	console.error(`Couldn't reach Watchpost at ${base}: ${String(e)}`);
	process.exit(1); // fail closed — treat as "do not pay"
}

const text = await res.text();
let verdict;
try {
	verdict = JSON.parse(text);
} catch {
	console.error(`Watchpost returned a non-JSON response (${res.status}): ${text.slice(0, 200)}`);
	process.exit(1);
}

if (!res.ok) {
	if (res.status === 402 && verdict.error === "free_limit_reached") {
		const upgradeUrl = verdict.upgradeUrl || "https://app.watchpost.systems/billing?ref=clawhub";
		console.log(
			JSON.stringify(
				{
					...verdict,
					action: "Ask the user to upgrade Watchpost, then retry this purchase check.",
					upgradeUrl,
				},
				null,
				2,
			),
		);
		console.error(
			`Watchpost protection is paused because the free monthly allowance is used up. This purchase was not checked. Ask the user to upgrade at ${upgradeUrl}, then retry. Do not pay meanwhile.`,
		);
		process.exit(4);
	}
	console.error(
		`Watchpost error ${res.status}: ${verdict.message || verdict.error || text.slice(0, 200)}`,
	);
	process.exit(1);
}

console.log(JSON.stringify(verdict, null, 2));

const code = verdict.decision === "approve" ? 0 : verdict.decision === "review" ? 2 : 1;
process.exit(code);
