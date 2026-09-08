// registry.mjs — map a store name → adapter instance.
//
// The orchestrator resolves `--store <name>` through here. Default store is
// "amazon" (behaviour-preserving). Add new stores in Phase 1 by importing the
// adapter and adding it to the factory map.

import { AmazonAdapter } from "./AmazonAdapter.mjs";
import { MilanunciosAdapter } from "./MilanunciosAdapter.mjs";
import { WallapopAdapter } from "./WallapopAdapter.mjs";

export const DEFAULT_STORE = "amazon";

// name → factory (lazy instance, one per resolve call).
const FACTORIES = Object.freeze({
  amazon: () => new AmazonAdapter(),
  milanuncios: () => new MilanunciosAdapter(),
  wallapop: () => new WallapopAdapter(),
});

export function knownStores() {
  return Object.keys(FACTORIES);
}

export function isKnownStore(name) {
  return Object.prototype.hasOwnProperty.call(FACTORIES, String(name).toLowerCase());
}

// Resolve a store name to a fresh adapter instance. Throws a clear error for
// an unknown store so the CLI can surface it.
export function resolveAdapter(name = DEFAULT_STORE) {
  const key = String(name || DEFAULT_STORE).toLowerCase();
  const factory = FACTORIES[key];
  if (!factory) {
    throw new Error(`unknown store "${name}" (known: ${knownStores().join(", ")})`);
  }
  return factory();
}

export default resolveAdapter;
