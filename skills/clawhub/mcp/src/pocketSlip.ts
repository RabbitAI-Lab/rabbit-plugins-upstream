import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import { randomBytes } from 'node:crypto';
import {
  bytesToBigInt,
  bytesToHex,
  createPublicClient,
  formatUnits,
  getAddress,
  http,
  isAddress,
  keccak256,
  parseUnits,
  stringToHex,
  type Address,
  type Hex,
  type WalletClient,
} from 'viem';
import { base } from 'viem/chains';
import { privateKeyToAccount } from 'viem/accounts';
import {
  BoundedAgentPolicy,
  CANONICAL_VAULT_V33_ADDRESS,
  CIRCLE_TOKEN_PAYMASTER_V08_ADDRESS,
  ERC20_PERMIT_EIP3009_ABI,
  ISSUE_VAULT,
  MIN_CIRCLE_PAYMASTER_USDC_UNITS,
  NARA_LIQUIDITY_HOOK_V5_ADDRESS,
  SlipMutex,
  SlipStatus,
  USDC_BASE_ADDRESS,
  createPolicyGuardedSigner,
  createSignedPaymentReceipt,
  createSlipSignerFromKey,
  decimalsForAsset,
  estimateUsdMicro,
  executeBatchPayoutSlips,
  formatReceiptCsvRow,
  fromViemWalletClient,
  grossUpForExactNet,
  keepSlip,
  minSlipAmount,
  normalizeSdkAsset,
  parsePopupCheckoutUrl,
  parseSlipUrl,
  parseWatchOnlyPosUrl,
  readOnChainSlip,
  redactSecretsFromToolOutput,
  refundSlipDirect,
  renderPrintableReceiptHtml,
  scanReclaimableSlips,
  splitAndPay,
  verifyPaymentReceiptOnChain,
  withdrawReferralCredits,
  type AnyAssetSymbol,
  type BaseCompatiblePublicClient,
  type BaseCompatibleWalletClient,
  type BoundedAgentPolicyConfig,
  type CreateSignedPaymentReceiptInput,
  type MintedPayoutSlipRecord,
  type PaymentReceiptBundleV1,
  type PayoutSlipItemInput,
  type PolicySnapshot,
  type ReceiptVerificationPublicClient,
  type SdkAssetSymbol,
  type SharedTransportExecutionOptions,
  type VaultTag,
  type VerifyPaymentReceiptOptions,
} from '@cryptoslip/sdk';

const SECP256K1_ORDER = 0xfffffffffffffffffffffffffffffffebaaedce6af48a03bbfd25e8cd0364141n;

export class PocketSlipError extends Error {
  constructor(message: string) {
    super(message);
    this.name = 'PocketSlipError';
  }
}

export interface PocketSlipPersistedState {
  version: 1;
  originalLineageHash: Hex;
  activeSlipId: string | null;
  vault: VaultTag;
  asset: SdkAssetSymbol;
  activeClaimPrivateKey?: Hex;
  activeClaimSigner?: Address;
  operatorPrivateKey: Hex;
  operatorAddress: Address;
  bootRotated: boolean;
  bootRotationTxHash?: Hex;
  updatedAt: string;
  createdRevocableSlipIds: string[];
}

export interface PocketSlipVaultConfig {
  /** `#startapp=slip_...` pocket-money URL (defaults to `process.env.CRYPTOSLIP_URL`). */
  slipUrl?: string;
  /** Local `0600` JSON file persisting the rotated key across restarts (`null` disables disk I/O). */
  stateFilePath?: string | null;
  /** Base Mainnet JSON-RPC endpoint (defaults to `process.env.CRYPTOSLIP_RPC_URL` or `https://mainnet.base.org`). */
  rpcUrl?: string;
  /** Injectable `viem` PublicClient for Base Mainnet (`8453`) or fork tests. */
  publicClient?: BaseCompatiblePublicClient;
  /** Optional `viem` WalletClient for direct EOA submission when desired. */
  walletClient?: BaseCompatibleWalletClient;
  /** Optional local operator key (`0x` + 64 hex); auto-generated and persisted (`0600`) if omitted. */
  operatorPrivateKey?: Hex;
  /** Out-of-context policy guard or config. */
  policy?: BoundedAgentPolicy | BoundedAgentPolicyConfig;
  /** Shared per-slip mutex (`V-03`). */
  mutex?: SlipMutex;
  /** Optional transport overrides (`bundlerFetch`, `relayClient`, `directBroadcast`, etc.). */
  transportOverrides?: Partial<SharedTransportExecutionOptions>;
  /** Optional injectable mint executor for tests or custom relayer pipelines. */
  customBatchExecutor?: typeof executeBatchPayoutSlips;
}

export interface BootRotateResult {
  bootRotated: boolean;
  resumedFromLocalState: boolean;
  slipId: string;
  vault: VaultTag;
  asset: SdkAssetSymbol;
  balanceUnits: string;
  humanBalance: string;
  activeClaimSigner: Address;
  operatorAddress: Address;
  bootRotationTxHash?: Hex;
}

export interface PocketSlipStatusSummary {
  initialized: boolean;
  hasActivePocketSlip: boolean;
  chainId: 8453;
  vault: VaultTag;
  vaultAddress: Address;
  paymasterDefault: Address;
  naraHookEnforced: Address;
  slipId: string | null;
  asset: SdkAssetSymbol | null;
  balanceUnits: string;
  humanBalance: string;
  bootRotated: boolean;
  bootRotationTxHash?: Hex;
  activeClaimSigner: Address | null;
  operatorAddress: Address;
  trackedRevocableSlipIds: string[];
  policy: PolicySnapshot;
}

export interface PayHumanInput {
  /** Human decimal string (e.g. `"1.50"`) or atomic integer string/bigint when `amountIsAtomic` is true. */
  amount: string | number | bigint;
  amountIsAtomic?: boolean;
  asset?: AnyAssetSymbol;
  /** `true` sets `cancelLockedUntil = 9_999_999_999` (irrevocable); `false` allows `0%`-fee creator reclaim if unclaimed. */
  noTakeBack?: boolean;
  mode?: 'open' | 'code';
  grossUpForExitFee?: boolean;
  note?: string;
  recipientLabel?: string;
}

export interface PayHumanResult {
  slipId: string;
  vault: VaultTag;
  asset: SdkAssetSymbol;
  humanAmount: number;
  grossAmountUnits: string;
  guaranteedNetClaimUnits: string;
  mode: 'open' | 'code';
  noTakeBack: boolean;
  outboundSlipUrl: string;
  claimCode?: string;
  txHash: Hex;
  splitTxHash?: Hex;
  deliveryNotice: string;
}

export interface BatchPayoutToolInput {
  items: Array<{
    amount: string | number | bigint;
    amountIsAtomic?: boolean;
    asset?: AnyAssetSymbol;
    noTakeBack?: boolean;
    grossUpForExitFee?: boolean;
    mode?: 'open' | 'code';
    note?: string;
    recipientRef?: string;
  }>;
  format?: 'json' | 'csv' | 'both';
}

export interface PayMerchantOrX402Input {
  /** Checksummed/hex `0x...` address, `#startapp=pos_<addr>`, or `#startapp=pay_<addr>_...` link. */
  recipient: string;
  /** Human decimal string (e.g. `"0.25"`) or atomic units when `amountIsAtomic` is true. */
  amount: string | number | bigint;
  amountIsAtomic?: boolean;
  /** Optional HTTPS URL of the HTTP `402` API endpoint (checked against `allowedDomains`). */
  endpointUrl?: string;
  /** Allows sweeping sub-minimum `< $0.10` remainder to merchant when explicitly enabled. */
  allowFullCashOnDust?: boolean;
}

function generateRandomSecp256k1Key(): Hex {
  for (let i = 0; i < 64; i++) {
    const bytes = randomBytes(32);
    const scalar = bytesToBigInt(bytes);
    if (scalar > 0n && scalar < SECP256K1_ORDER) {
      return bytesToHex(bytes);
    }
  }
  throw new PocketSlipError('Failed to generate valid secp256k1 key.');
}

function parseEnvUsdToMicro(raw: string | undefined, fallbackMicro: bigint): bigint {
  if (!raw || !raw.trim()) return fallbackMicro;
  return parseUnits(raw.trim(), 6);
}

export function buildPolicyFromEnv(
  env: NodeJS.ProcessEnv = process.env,
  overrides?: BoundedAgentPolicyConfig,
): BoundedAgentPolicy {
  const maxPerCallUsdMicro =
    overrides?.maxPerCallUsdMicro ??
    parseEnvUsdToMicro(env.CRYPTOSLIP_MAX_PER_CALL_USD, 500_000n);
  const maxDailyUsdMicro =
    overrides?.maxDailyUsdMicro ??
    parseEnvUsdToMicro(env.CRYPTOSLIP_MAX_DAILY_USD, 5_000_000n);
  const maxSpendsPerMinute =
    overrides?.maxSpendsPerMinute ??
    (env.CRYPTOSLIP_MAX_SPENDS_PER_MIN
      ? Number.parseInt(env.CRYPTOSLIP_MAX_SPENDS_PER_MIN, 10)
      : 3);

  const allowedRecipients =
    overrides?.allowedRecipients ??
    (env.CRYPTOSLIP_ALLOWED_RECIPIENTS
      ? env.CRYPTOSLIP_ALLOWED_RECIPIENTS.split(',').map((s) => s.trim()).filter(Boolean)
      : undefined);

  const allowedDomains =
    overrides?.allowedDomains ??
    (env.CRYPTOSLIP_ALLOWED_DOMAINS
      ? env.CRYPTOSLIP_ALLOWED_DOMAINS.split(',').map((s) => s.trim()).filter(Boolean)
      : undefined);

  const allowOutboundSlipLinks =
    overrides?.allowOutboundSlipLinks ??
    (env.CRYPTOSLIP_ALLOW_OUTBOUND_LINKS
      ? env.CRYPTOSLIP_ALLOW_OUTBOUND_LINKS.toLowerCase() !== 'false'
      : true);

  return new BoundedAgentPolicy({
    ...overrides,
    maxPerCallUsdMicro,
    maxDailyUsdMicro,
    maxSpendsPerMinute,
    allowedRecipients,
    allowedDomains,
    allowOutboundSlipLinks,
  });
}

function parseAmountUnits(
  raw: string | number | bigint,
  asset: SdkAssetSymbol,
  amountIsAtomic = false,
): bigint {
  if (typeof raw === 'bigint') return raw;
  if (amountIsAtomic) {
    const str = String(raw).trim();
    if (!/^\d+$/.test(str)) {
      throw new PocketSlipError(`Invalid atomic integer amount: ${str}`);
    }
    return BigInt(str);
  }
  const str = String(raw).trim();
  if (!/^\d+(?:\.\d+)?$/.test(str)) {
    throw new PocketSlipError(`Invalid decimal amount: ${str}`);
  }
  return parseUnits(str, decimalsForAsset(asset));
}

function resolveMerchantAddress(rawRecipient: string): Address {
  const trimmed = rawRecipient.trim();
  if (isAddress(trimmed)) {
    return getAddress(trimmed);
  }
  const pos = parseWatchOnlyPosUrl(trimmed);
  if (pos?.merchantAddress && isAddress(pos.merchantAddress)) {
    return getAddress(pos.merchantAddress);
  }
  const checkout = parsePopupCheckoutUrl(trimmed);
  if (checkout?.recipientAddress && isAddress(checkout.recipientAddress)) {
    return getAddress(checkout.recipientAddress);
  }
  throw new PocketSlipError(
    'Recipient must be a valid 0x Base wallet address, #startapp=pos_<address>, or #startapp=pay_<address> URL.',
  );
}

/**
 * `PocketSlipVault` (`Module #1`):
 * Self-rotating `$5` pocket-money vault for AI agents (`V-01` `<1s` Boot Auto-Keep,
 * `V-02` `BoundedAgentPolicy` firewall, `V-03` `SlipMutex` + `$0.10` dust guard,
 * and `V-04` Circle `TokenPaymasterV08` USDC gas default).
 */
export class PocketSlipVault {
  readonly publicClient: BaseCompatiblePublicClient;
  readonly policy: BoundedAgentPolicy;
  readonly mutex: SlipMutex;
  readonly stateFilePath: string | null;

  private readonly rawSlipUrl?: string;
  private readonly walletClient?: BaseCompatibleWalletClient;
  private readonly transportOverrides: Partial<SharedTransportExecutionOptions>;
  private readonly customBatchExecutor: typeof executeBatchPayoutSlips;

  private operatorPrivateKey: Hex;
  private operatorAddress: Address;
  private originalLineageHash: Hex;
  private activeSlipId: string | null = null;
  private activeVault: VaultTag = ISSUE_VAULT;
  private activeAsset: SdkAssetSymbol = 'USDC';
  private activeClaimPrivateKey?: Hex;
  private activeClaimSigner?: Address;
  private bootRotated = false;
  private bootRotationTxHash?: Hex;
  private createdRevocableSlipIds: string[] = [];
  private bootPromise: Promise<BootRotateResult | null> | null = null;
  private initialized = false;

  constructor(config: PocketSlipVaultConfig = {}) {
    this.rawSlipUrl = config.slipUrl ?? process.env.CRYPTOSLIP_URL;
    const defaultStateFile =
      process.env.CRYPTOSLIP_STATE_PATH ??
      path.join(os.homedir(), '.cryptoslip-mcp', 'pocket-state.json');
    this.stateFilePath =
      config.stateFilePath === undefined ? defaultStateFile : config.stateFilePath;

    const rpcUrl =
      config.rpcUrl ?? process.env.CRYPTOSLIP_RPC_URL ?? 'https://mainnet.base.org';
    this.publicClient =
      config.publicClient ??
      createPublicClient({
        chain: base,
        transport: http(rpcUrl),
      });

    this.walletClient = config.walletClient;
    this.policy =
      config.policy instanceof BoundedAgentPolicy
        ? config.policy
        : buildPolicyFromEnv(process.env, config.policy);
    this.mutex = config.mutex ?? new SlipMutex();
    this.transportOverrides = config.transportOverrides ?? {};
    this.customBatchExecutor = config.customBatchExecutor ?? executeBatchPayoutSlips;

    const persisted = this.readPersistedState();
    const initialOpKey =
      config.operatorPrivateKey ??
      (this.walletClient?.account && 'source' in this.walletClient.account
        ? undefined
        : persisted?.operatorPrivateKey) ??
      generateRandomSecp256k1Key();

    this.operatorPrivateKey = (
      initialOpKey.startsWith('0x') ? initialOpKey : `0x${initialOpKey}`
    ) as Hex;
    this.operatorAddress = this.walletClient?.account
      ? getAddress(this.walletClient.account.address)
      : getAddress(privateKeyToAccount(this.operatorPrivateKey).address);
    this.originalLineageHash = persisted?.originalLineageHash ?? ('0x' + '00'.repeat(32)) as Hex;
    if (persisted?.createdRevocableSlipIds) {
      this.createdRevocableSlipIds = [...persisted.createdRevocableSlipIds];
    }
  }

  private readPersistedState(): PocketSlipPersistedState | null {
    if (!this.stateFilePath) return null;
    try {
      if (!fs.existsSync(this.stateFilePath)) return null;
      const raw = fs.readFileSync(this.stateFilePath, 'utf8');
      const parsed = JSON.parse(raw) as PocketSlipPersistedState;
      if (parsed && parsed.version === 1 && parsed.operatorPrivateKey) {
        return parsed;
      }
      return null;
    } catch {
      return null;
    }
  }

  private writePersistedState(state: PocketSlipPersistedState): void {
    if (!this.stateFilePath) return;
    const dir = path.dirname(this.stateFilePath);
    fs.mkdirSync(dir, { recursive: true, mode: 0o700 });
    const tmpPath = `${this.stateFilePath}.${process.pid}.tmp`;
    fs.writeFileSync(tmpPath, JSON.stringify(state, null, 2), {
      encoding: 'utf8',
      mode: 0o600,
    });
    try {
      fs.chmodSync(tmpPath, 0o600);
    } catch {
      // Windows NTFS ignores POSIX mode bits; chmod succeeds on Linux/macOS
    }
    fs.renameSync(tmpPath, this.stateFilePath);
  }

  private syncStateToDisk(): void {
    this.writePersistedState({
      version: 1,
      originalLineageHash: this.originalLineageHash,
      activeSlipId: this.activeSlipId,
      vault: this.activeVault,
      asset: this.activeAsset,
      ...(this.activeClaimPrivateKey ? { activeClaimPrivateKey: this.activeClaimPrivateKey } : {}),
      ...(this.activeClaimSigner ? { activeClaimSigner: this.activeClaimSigner } : {}),
      operatorPrivateKey: this.operatorPrivateKey,
      operatorAddress: this.operatorAddress,
      bootRotated: this.bootRotated,
      ...(this.bootRotationTxHash ? { bootRotationTxHash: this.bootRotationTxHash } : {}),
      updatedAt: new Date().toISOString(),
      createdRevocableSlipIds: this.createdRevocableSlipIds,
    });
  }

  /**
   * `V-01` Boot Auto-Keep:
   * Immediately checks the configured `CRYPTOSLIP_URL` on Base Mainnet. If unrotated (`nonces == 0`),
   * executes `keepSlip()` (`0%` protocol fee) rotating `claimSigner` to a fresh local key persisted in
   * `0600` local storage, invalidating the `.env` `#k` link on-chain in `<1s`.
   */
  async bootAndRotate(): Promise<BootRotateResult | null> {
    if (this.bootPromise) return this.bootPromise;
    this.bootPromise = this.performBootAndRotate();
    try {
      return await this.bootPromise;
    } catch (err) {
      this.bootPromise = null;
      throw err;
    }
  }

  private async performBootAndRotate(): Promise<BootRotateResult | null> {
    const persisted = this.readPersistedState();

    if (!this.rawSlipUrl || !this.rawSlipUrl.trim()) {
      if (persisted?.activeSlipId && persisted.activeClaimPrivateKey) {
        const onChain = await readOnChainSlip({
          publicClient: this.publicClient,
          slipId: persisted.activeSlipId,
          vault: persisted.vault,
        });
        if (
          onChain.status === SlipStatus.ACTIVE &&
          persisted.activeClaimSigner &&
          onChain.claimSigner.toLowerCase() === persisted.activeClaimSigner.toLowerCase()
        ) {
          this.activeSlipId = persisted.activeSlipId;
          this.activeVault = persisted.vault;
          this.activeAsset = onChain.asset;
          this.activeClaimPrivateKey = persisted.activeClaimPrivateKey;
          this.activeClaimSigner = persisted.activeClaimSigner;
          this.bootRotated = persisted.bootRotated;
          this.bootRotationTxHash = persisted.bootRotationTxHash;
          this.initialized = true;
          return {
            bootRotated: false,
            resumedFromLocalState: true,
            slipId: this.activeSlipId,
            vault: this.activeVault,
            asset: this.activeAsset,
            balanceUnits: onChain.amount.toString(),
            humanBalance: formatUnits(onChain.amount, decimalsForAsset(onChain.asset)),
            activeClaimSigner: this.activeClaimSigner,
            operatorAddress: this.operatorAddress,
            ...(this.bootRotationTxHash ? { bootRotationTxHash: this.bootRotationTxHash } : {}),
          };
        }
      }
      this.initialized = true;
      return null;
    }

    const parsed = parseSlipUrl(this.rawSlipUrl);
    if (!parsed || parsed.mode !== 'open' || !parsed.claimKey || !parsed.claimAddress) {
      throw new PocketSlipError(
        'CRYPTOSLIP_URL must be an open #startapp=slip_... URL carrying a # fragment claim key.',
      );
    }

    const lineageHash = keccak256(stringToHex(`${parsed.vault}:${parsed.id}`));
    this.originalLineageHash = lineageHash;

    // 1. Resume from local 0600 rotated state if matching lineage and still active on-chain
    if (
      persisted &&
      persisted.originalLineageHash === lineageHash &&
      persisted.activeSlipId &&
      persisted.activeClaimPrivateKey &&
      persisted.activeClaimSigner
    ) {
      const resumedSlip = await readOnChainSlip({
        publicClient: this.publicClient,
        slipId: persisted.activeSlipId,
        vault: persisted.vault,
      });
      if (
        resumedSlip.status === SlipStatus.ACTIVE &&
        resumedSlip.claimSigner.toLowerCase() === persisted.activeClaimSigner.toLowerCase()
      ) {
        this.activeSlipId = persisted.activeSlipId;
        this.activeVault = persisted.vault;
        this.activeAsset = resumedSlip.asset;
        this.activeClaimPrivateKey = persisted.activeClaimPrivateKey;
        this.activeClaimSigner = persisted.activeClaimSigner;
        this.bootRotated = persisted.bootRotated;
        this.bootRotationTxHash = persisted.bootRotationTxHash;
        this.initialized = true;
        return {
          bootRotated: false,
          resumedFromLocalState: true,
          slipId: this.activeSlipId,
          vault: this.activeVault,
          asset: this.activeAsset,
          balanceUnits: resumedSlip.amount.toString(),
          humanBalance: formatUnits(resumedSlip.amount, decimalsForAsset(resumedSlip.asset)),
          activeClaimSigner: this.activeClaimSigner,
          operatorAddress: this.operatorAddress,
          ...(this.bootRotationTxHash ? { bootRotationTxHash: this.bootRotationTxHash } : {}),
        };
      }
    }

    // 2. Inspect initial slip on Base
    const initialOnChain = await readOnChainSlip({
      publicClient: this.publicClient,
      slipId: parsed.id,
      vault: parsed.vault,
    });

    if (initialOnChain.status !== SlipStatus.ACTIVE) {
      throw new PocketSlipError(
        `PocketSlip #${parsed.id} is not active on Base (status=${initialOnChain.status}).`,
      );
    }
    if (initialOnChain.claimSigner.toLowerCase() !== parsed.claimAddress.toLowerCase()) {
      throw new PocketSlipError(
        `PocketSlip #${parsed.id} claimSigner on-chain does not match CRYPTOSLIP_URL (already rotated by another host).`,
      );
    }

    // 3. V-01 Mandatory Boot Auto-Keep when slip is unrotated (`nonces == 0`)
    if (initialOnChain.nonce === 0n && !initialOnChain.refundFeeRequired) {
      const guardedInitialSigner = createPolicyGuardedSigner(
        createSlipSignerFromKey(parsed.claimKey),
        this.policy,
        { slipAsset: initialOnChain.asset },
      );

      const kept = await keepSlip({
        publicClient: this.publicClient,
        slipId: parsed.id,
        vault: parsed.vault,
        claimSigner: guardedInitialSigner,
        userMainWallet: this.operatorAddress,
        mode: 'agent',
        isBootKeep: true,
        mutex: this.mutex,
        ...this.transportOverrides,
        onBeforeBroadcast: ({ newClaimPrivateKey, newClaimSigner }) => {
          this.activeSlipId = parsed.id;
          this.activeVault = parsed.vault;
          this.activeAsset = initialOnChain.asset;
          this.activeClaimPrivateKey = newClaimPrivateKey;
          this.activeClaimSigner = newClaimSigner;
          this.bootRotated = true;
          this.syncStateToDisk();
        },
      });

      this.activeSlipId = kept.slipId.toString();
      this.activeVault = kept.vault;
      this.activeAsset = initialOnChain.asset;
      this.activeClaimPrivateKey = kept.newClaimPrivateKey;
      this.activeClaimSigner = kept.newClaimSigner;
      this.bootRotated = true;
      this.bootRotationTxHash = kept.txHash;
      this.initialized = true;
      this.syncStateToDisk();

      return {
        bootRotated: true,
        resumedFromLocalState: false,
        slipId: this.activeSlipId,
        vault: this.activeVault,
        asset: this.activeAsset,
        balanceUnits: kept.netAmountUnits.toString(),
        humanBalance: formatUnits(kept.netAmountUnits, decimalsForAsset(initialOnChain.asset)),
        activeClaimSigner: this.activeClaimSigner,
        operatorAddress: this.operatorAddress,
        bootRotationTxHash: kept.txHash,
      };
    }

    // Already rotated (`nonces > 0`) to the key supplied in CRYPTOSLIP_URL
    this.activeSlipId = parsed.id;
    this.activeVault = parsed.vault;
    this.activeAsset = initialOnChain.asset;
    this.activeClaimPrivateKey = parsed.claimKey;
    this.activeClaimSigner = parsed.claimAddress;
    this.bootRotated = false;
    this.initialized = true;
    this.syncStateToDisk();

    return {
      bootRotated: false,
      resumedFromLocalState: false,
      slipId: this.activeSlipId,
      vault: this.activeVault,
      asset: this.activeAsset,
      balanceUnits: initialOnChain.amount.toString(),
      humanBalance: formatUnits(initialOnChain.amount, decimalsForAsset(initialOnChain.asset)),
      activeClaimSigner: this.activeClaimSigner,
      operatorAddress: this.operatorAddress,
    };
  }

  private async ensureBooted(): Promise<void> {
    if (!this.initialized) {
      await this.bootAndRotate();
    }
  }

  /**
   * Tool #1: `cryptoslip_status` — Safe redacted slip/wallet balance, vault `v33`, and policy limits.
   */
  async getStatus(): Promise<PocketSlipStatusSummary> {
    await this.ensureBooted();

    let balanceUnits = '0';
    let humanBalance = '0';

    if (this.activeSlipId) {
      const state = await readOnChainSlip({
        publicClient: this.publicClient,
        slipId: this.activeSlipId,
        vault: this.activeVault,
      });
      if (state.status === SlipStatus.ACTIVE) {
        balanceUnits = state.amount.toString();
        humanBalance = formatUnits(state.amount, decimalsForAsset(state.asset));
        this.activeAsset = state.asset;
      } else {
        this.activeSlipId = null;
      }
    }

    const rawSummary: PocketSlipStatusSummary = {
      initialized: this.initialized,
      hasActivePocketSlip: Boolean(this.activeSlipId),
      chainId: 8453,
      vault: this.activeVault,
      vaultAddress: CANONICAL_VAULT_V33_ADDRESS,
      paymasterDefault: CIRCLE_TOKEN_PAYMASTER_V08_ADDRESS,
      naraHookEnforced: NARA_LIQUIDITY_HOOK_V5_ADDRESS,
      slipId: this.activeSlipId,
      asset: this.activeSlipId ? this.activeAsset : null,
      balanceUnits,
      humanBalance,
      bootRotated: this.bootRotated,
      ...(this.bootRotationTxHash ? { bootRotationTxHash: this.bootRotationTxHash } : {}),
      activeClaimSigner: this.activeClaimSigner ?? null,
      operatorAddress: this.operatorAddress,
      trackedRevocableSlipIds: [...this.createdRevocableSlipIds],
      policy: this.policy.getSnapshot(),
    };

    return this.policy.redactOutput(rawSummary, {
      allowedPublicHashFields: ['bootRotationTxHash'],
    });
  }

  /**
   * Tool #2: `cryptoslip_pay_human` — Mints or splits a `No take-back` or revocable `#startapp=slip_...`
   * link (or 12-char `scrypt` code) for X/Telegram/SMS human bounties.
   */
  async payHuman(input: PayHumanInput): Promise<PayHumanResult> {
    await this.ensureBooted();
    this.policy.assertCanEmitOutboundSlipLink();

    const asset = normalizeSdkAsset(input.asset ?? this.activeAsset ?? 'USDC');
    const requestedUnits = parseAmountUnits(input.amount, asset, input.amountIsAtomic);
    const grossMintUnits = input.grossUpForExitFee
      ? grossUpForExactNet(requestedUnits)
      : requestedUnits;
    const minUnits = minSlipAmount(asset, this.activeVault);
    if (grossMintUnits < minUnits) {
      throw new PocketSlipError(
        `Amount ${grossMintUnits.toString()} raw ${asset} is below ${this.activeVault} minimum (${minUnits.toString()}).`,
      );
    }

    let splitTxHash: Hex | undefined;

    // If operating from an active PocketSlip without an externally funded walletClient,
    // split the required funding slice from the PocketSlip into operatorAddress first,
    // then mint the recipient's slip via Circle TokenPaymasterV08 / batch executor.
    if (this.activeSlipId && this.activeClaimPrivateKey && !this.walletClient) {
      let targetNetToOperator = grossMintUnits;
      if (asset === 'USDC' && this.activeAsset === 'USDC') {
        let operatorUsdc: bigint | null = null;
        try {
          const rawBal = await this.publicClient.readContract({
            address: USDC_BASE_ADDRESS,
            abi: ERC20_PERMIT_EIP3009_ABI,
            functionName: 'balanceOf',
            args: [this.operatorAddress],
          });
          if (typeof rawBal === 'bigint') operatorUsdc = rawBal;
        } catch {
          operatorUsdc = null;
        }
        if (operatorUsdc !== null && operatorUsdc < MIN_CIRCLE_PAYMASTER_USDC_UNITS) {
          const gasDeficit = MIN_CIRCLE_PAYMASTER_USDC_UNITS - operatorUsdc;
          const candidateFunding = grossUpForExactNet(grossMintUnits + gasDeficit);
          const slipState = await readOnChainSlip({
            publicClient: this.publicClient,
            slipId: this.activeSlipId,
            vault: this.activeVault,
          });
          const rem = slipState.amount - candidateFunding;
          const fitsWithoutDust =
            rem === 0n || rem >= minSlipAmount(slipState.asset, this.activeVault);
          const fitsPerCallCap =
            estimateUsdMicro(candidateFunding, slipState.asset) <=
            this.policy.maxPerCallUsdMicro;
          if (slipState.amount >= candidateFunding && fitsWithoutDust && fitsPerCallCap) {
            targetNetToOperator = grossMintUnits + gasDeficit;
          }
        }
      }

      const fundingNeeded = grossUpForExactNet(targetNetToOperator);
      const guardedPocketSigner = createPolicyGuardedSigner(
        createSlipSignerFromKey(this.activeClaimPrivateKey),
        this.policy,
        {
          slipAsset: this.activeAsset,
          allowInternalRecipient: this.operatorAddress,
        },
      );

      const splitRes = await splitAndPay({
        publicClient: this.publicClient,
        slipId: this.activeSlipId,
        vault: this.activeVault,
        claimSigner: guardedPocketSigner,
        paymentAmount: fundingNeeded,
        merchant: this.operatorAddress,
        mode: 'agent',
        paymasterSignerKey: this.operatorPrivateKey,
        mutex: this.mutex,
        ...this.transportOverrides,
        onBeforeBroadcast: ({ newChangePrivateKey, newChangeSigner, expectedChangeAmount }) => {
          if (expectedChangeAmount > 0n && newChangePrivateKey) {
            this.activeClaimPrivateKey = newChangePrivateKey;
            this.activeClaimSigner = newChangeSigner;
            this.syncStateToDisk();
          }
        },
      });

      splitTxHash = splitRes.txHash;
      if (splitRes.changeAmount > 0n && splitRes.changeSlipId !== null && splitRes.newChangePrivateKey) {
        this.activeSlipId = splitRes.changeSlipId.toString();
        this.activeClaimPrivateKey = splitRes.newChangePrivateKey;
        this.activeClaimSigner = splitRes.newChangeSigner;
      } else if (splitRes.changeAmount === 0n) {
        this.activeSlipId = null;
        this.activeClaimPrivateKey = undefined;
        this.activeClaimSigner = undefined;
      }
      this.syncStateToDisk();
    } else {
      // Wallet-funded path: enforce policy spend cap on the guarded operator signer
      this.policy.authorizeAndRecordSpend({
        amount: grossMintUnits,
        asset,
        dedupKey: `pay_human:${Date.now()}:${grossMintUnits.toString()}`,
      });
    }

    const signerForMint = this.walletClient
      ? fromViemWalletClient(this.walletClient as unknown as WalletClient)
      : createSlipSignerFromKey(this.operatorPrivateKey);

    const batchRes = await this.customBatchExecutor({
      publicClient: this.publicClient,
      ...(this.walletClient ? { walletClient: this.walletClient } : {}),
      signer: signerForMint,
      paymasterSignerKey: this.operatorPrivateKey,
      useCirclePaymaster: !this.walletClient,
      bundlerUrls: this.transportOverrides.bundlerUrls,
      bundlerFetch: this.transportOverrides.bundlerFetch,
      vault: this.activeVault,
      items: [
        {
          amount: grossMintUnits,
          asset,
          noTakeBack: Boolean(input.noTakeBack),
          grossUpForExitFee: false,
          mode: input.mode ?? 'open',
          note: input.note,
          recipientRef: input.recipientLabel,
        },
      ],
    });

    const minted = batchRes.mintedSlips[0];
    if (!minted) {
      throw new PocketSlipError('Batch mint succeeded without returning a minted slip record.');
    }

    if (!input.noTakeBack) {
      this.createdRevocableSlipIds.push(minted.slipId);
      this.syncStateToDisk();
    }

    const out: PayHumanResult = {
      slipId: minted.slipId,
      vault: minted.vault,
      asset: minted.asset,
      humanAmount: minted.humanAmount,
      grossAmountUnits: minted.grossAmountUnits,
      guaranteedNetClaimUnits: minted.guaranteedNetClaimUnits,
      mode: minted.mode,
      noTakeBack: Boolean(input.noTakeBack),
      outboundSlipUrl: minted.url,
      ...(minted.claimCode ? { claimCode: minted.claimCode } : {}),
      txHash: minted.txHash,
      ...(splitTxHash ? { splitTxHash } : {}),
      deliveryNotice:
        minted.mode === 'code'
          ? 'Send outboundSlipUrl and the 12-character claimCode over separate channels (or release claimCode upon task verification).'
          : 'Deliver outboundSlipUrl strictly inside a private DM (Telegram, X DM, or SMS). Never post open # links in public timelines.',
    };

    return this.policy.redactOutput(out, {
      allowOutboundSlipLink: true,
      outboundFields: ['outboundSlipUrl'],
      allowedPublicHashFields: ['txHash', 'splitTxHash'],
    });
  }

  /**
   * Tool #3: `cryptoslip_batch_payout` — 1-Tx `Multicall3` batch dispenser (`1..500` items) returning JSON/CSV `#` links.
   */
  async batchPayout(input: BatchPayoutToolInput): Promise<{
    count: number;
    txHashes: readonly Hex[];
    outboundLinks?: readonly MintedPayoutSlipRecord[];
    outboundCsv?: string;
  }> {
    await this.ensureBooted();
    this.policy.assertCanEmitOutboundSlipLink();

    if (!input.items || input.items.length === 0 || input.items.length > 500) {
      throw new PocketSlipError('batchPayout requires between 1 and 500 items.');
    }

    const normalizedItems: PayoutSlipItemInput[] = [];
    let totalUsdMicro = 0n;

    for (const rawItem of input.items) {
      const asset = normalizeSdkAsset(rawItem.asset ?? 'USDC');
      const units = parseAmountUnits(rawItem.amount, asset, rawItem.amountIsAtomic);
      const grossUnits = rawItem.grossUpForExitFee ? grossUpForExactNet(units) : units;
      totalUsdMicro += estimateUsdMicro(grossUnits, asset);

      normalizedItems.push({
        amount: grossUnits,
        asset,
        noTakeBack: Boolean(rawItem.noTakeBack),
        grossUpForExitFee: false,
        mode: rawItem.mode ?? 'open',
        note: rawItem.note,
        recipientRef: rawItem.recipientRef,
      });
    }

    // Enforce aggregate batch USD budget & rate limit BEFORE signing any permit
    this.policy.authorizeAndRecordSpend({
      amount: totalUsdMicro,
      asset: 'USDC',
      dedupKey: `batch:${Date.now()}:${normalizedItems.length}`,
    });

    const signerForBatch = this.walletClient
      ? fromViemWalletClient(this.walletClient as unknown as WalletClient)
      : createSlipSignerFromKey(this.operatorPrivateKey);

    const batchRes = await this.customBatchExecutor({
      publicClient: this.publicClient,
      ...(this.walletClient ? { walletClient: this.walletClient } : {}),
      signer: signerForBatch,
      paymasterSignerKey: this.operatorPrivateKey,
      useCirclePaymaster: !this.walletClient,
      bundlerUrls: this.transportOverrides.bundlerUrls,
      bundlerFetch: this.transportOverrides.bundlerFetch,
      vault: this.activeVault,
      items: normalizedItems,
    });

    for (const m of batchRes.mintedSlips) {
      if (m.cancelLockedUntil === 0) {
        this.createdRevocableSlipIds.push(m.slipId);
      }
    }
    this.syncStateToDisk();

    const fmt = input.format ?? 'json';
    const rawOut = {
      count: batchRes.mintedSlips.length,
      txHashes: batchRes.txHashes,
      ...(fmt === 'json' || fmt === 'both' ? { outboundLinks: batchRes.mintedSlips } : {}),
      ...(fmt === 'csv' || fmt === 'both' ? { outboundCsv: batchRes.csv } : {}),
    };

    return this.policy.redactOutput(rawOut, {
      allowOutboundSlipLink: true,
      outboundFields: ['outboundLinks', 'outboundCsv', 'url', 'sovereignUrl'],
      allowedPublicHashFields: ['txHashes', 'txHash'],
    });
  }

  /**
   * Tool #4: `cryptoslip_pay_x402_or_merchant` — `splitAndPay` with `BoundedAgentPolicy` (`V-02`),
   * `SlipMutex` + `$0.10` dust guard (`V-03`), and Circle `TokenPaymasterV08` default (`V-04`).
   */
  async payMerchantOrX402(input: PayMerchantOrX402Input): Promise<{
    txHash: Hex;
    parentSlipId: string;
    newActiveSlipId: string | null;
    merchant: Address;
    asset: SdkAssetSymbol;
    grossPaymentUnits: string;
    feeUnits: string;
    netMerchantUnits: string;
    remainingChangeUnits: string;
    transportTier: string;
  }> {
    await this.ensureBooted();

    if (!this.activeSlipId || !this.activeClaimPrivateKey) {
      throw new PocketSlipError(
        'No active PocketSlip available. Provision CRYPTOSLIP_URL with an active slip first.',
      );
    }

    if (input.endpointUrl) {
      this.policy.assertAllowedDomain(input.endpointUrl);
    }

    const merchant = resolveMerchantAddress(input.recipient);
    this.policy.assertSafeDestination(merchant, this.activeClaimSigner);

    const paymentAmount = parseAmountUnits(
      input.amount,
      this.activeAsset,
      input.amountIsAtomic,
    );

    // Pre-wrap active slip signer with BoundedAgentPolicy so SplitPermit signature
    // enforces maxPerCallUsdMicro, maxSpendsPerMinute, maxDailyUsdMicro, and destination rules!
    const guardedSlipSigner = createPolicyGuardedSigner(
      createSlipSignerFromKey(this.activeClaimPrivateKey),
      this.policy,
      { slipAsset: this.activeAsset },
    );

    const res = await splitAndPay({
      publicClient: this.publicClient,
      slipId: this.activeSlipId,
      vault: this.activeVault,
      claimSigner: guardedSlipSigner,
      paymentAmount,
      merchant,
      allowFullCashOnDust: Boolean(input.allowFullCashOnDust),
      mode: 'agent', // V-04: defaults headless agent to Circle TokenPaymasterV08 / direct Base tx
      paymasterSignerKey: this.operatorPrivateKey,
      ...(this.walletClient ? { walletClient: this.walletClient } : {}),
      mutex: this.mutex,
      ...this.transportOverrides,
      onBeforeBroadcast: ({ newChangePrivateKey, newChangeSigner, expectedChangeAmount }) => {
        if (expectedChangeAmount > 0n && newChangePrivateKey) {
          this.activeClaimPrivateKey = newChangePrivateKey;
          this.activeClaimSigner = newChangeSigner;
          this.syncStateToDisk();
        }
      },
    });

    if (res.changeAmount > 0n && res.changeSlipId !== null && res.newChangePrivateKey) {
      this.activeSlipId = res.changeSlipId.toString();
      this.activeClaimPrivateKey = res.newChangePrivateKey;
      this.activeClaimSigner = res.newChangeSigner;
    } else if (res.changeAmount === 0n) {
      this.activeSlipId = null;
      this.activeClaimPrivateKey = undefined;
      this.activeClaimSigner = undefined;
    }
    this.syncStateToDisk();

    const summary = {
      txHash: res.txHash,
      parentSlipId: res.parentSlipId.toString(),
      newActiveSlipId: res.changeSlipId !== null ? res.changeSlipId.toString() : null,
      merchant: res.merchant,
      asset: res.asset,
      grossPaymentUnits: res.grossPaymentAmount.toString(),
      feeUnits: res.feeUnits.toString(),
      netMerchantUnits: res.netMerchantAmount.toString(),
      remainingChangeUnits: res.changeAmount.toString(),
      transportTier: res.transportTier,
    };

    return this.policy.redactOutput(summary, {
      allowedPublicHashFields: ['txHash'],
    });
  }

  /**
   * Tool #5: `cryptoslip_verify_or_export_receipt` — Verifies or generates `PaymentReceiptBundleV1`.
   */
  async verifyOrExportReceipt(
    input:
      | {
          action: 'verify';
          bundle: PaymentReceiptBundleV1;
          options?: VerifyPaymentReceiptOptions;
        }
      | {
          action: 'export';
          receiptInput: Omit<CreateSignedPaymentReceiptInput, 'signer'>;
          signWithOperatorKey?: boolean;
          includeCsv?: boolean;
          includeHtml?: boolean;
        },
  ): Promise<Record<string, unknown>> {
    if (input.action === 'verify') {
      const verification = await verifyPaymentReceiptOnChain(
        this.publicClient as unknown as ReceiptVerificationPublicClient,
        input.bundle,
        input.options,
      );
      return redactSecretsFromToolOutput(
        {
          action: 'verify',
          valid: verification.valid,
          reason: verification.reason,
          verifiedNetAmount: verification.verifiedNetAmount?.toString(),
          verifiedGrossAmount: verification.verifiedGrossAmount?.toString(),
          verifiedFeeAmount: verification.verifiedFeeAmount?.toString(),
          blockNumber: verification.blockNumber,
          blockTimestamp: verification.blockTimestamp,
          issuerVerified: verification.issuerVerified,
          builderCodePresent: verification.builderCodePresent,
        },
        { allowedPublicHashFields: ['txHash', 'orderDigest'] },
      );
    }

    const signer = input.signWithOperatorKey
      ? createPolicyGuardedSigner(createSlipSignerFromKey(this.operatorPrivateKey), this.policy)
      : undefined;

    const bundle = await createSignedPaymentReceipt({
      ...input.receiptInput,
      ...(signer ? { signer } : {}),
    });

    const out: Record<string, unknown> = {
      action: 'export',
      bundle,
      ...(input.includeCsv ? { csvRow: formatReceiptCsvRow(bundle) } : {}),
      ...(input.includeHtml ? { html: renderPrintableReceiptHtml(bundle) } : {}),
    };

    return redactSecretsFromToolOutput(out, {
      allowedPublicHashFields: ['txHash', 'orderDigest'],
    });
  }

  /**
   * Tool #6: `cryptoslip_reclaim_unclaimed` — `0%`-fee `refundSlipDirect` for unclaimed `cancelLockedUntil == 0` DM slips.
   */
  async reclaimUnclaimed(input: {
    slipId?: string;
    scanOnly?: boolean;
    minAgeSeconds?: number;
  }): Promise<Record<string, unknown>> {
    await this.ensureBooted();

    if (input.scanOnly || !input.slipId) {
      const reclaimable = await scanReclaimableSlips({
        publicClient: this.publicClient,
        creator: this.operatorAddress,
        vault: this.activeVault,
        ...(this.createdRevocableSlipIds.length > 0
          ? { candidateSlipIds: this.createdRevocableSlipIds }
          : {}),
        minAgeSeconds: input.minAgeSeconds ?? 0,
      });

      if (input.scanOnly || reclaimable.length === 0) {
        return this.policy.redactOutput({
          mode: 'scan',
          reclaimableCount: reclaimable.length,
          reclaimable: reclaimable.map((r) => ({
            slipId: r.slipId.toString(),
            vault: r.vault,
            asset: r.asset,
            amountUnits: r.amount.toString(),
            ageSeconds: r.ageSeconds,
          })),
        });
      }

      // Reclaim the first discovered slip if slipId wasn't explicitly specified and scanOnly is false
      const target = reclaimable[0]!;
      const refunded = await refundSlipDirect({
        publicClient: this.publicClient,
        slipId: target.slipId,
        vault: target.vault,
        ...(this.walletClient ? { walletClient: this.walletClient } : {}),
        paymasterSignerKey: this.operatorPrivateKey,
        useCirclePaymaster: !this.walletClient,
        bundlerUrls: this.transportOverrides.bundlerUrls,
        bundlerFetch: this.transportOverrides.bundlerFetch,
        mutex: this.mutex,
      });

      this.createdRevocableSlipIds = this.createdRevocableSlipIds.filter(
        (id) => id !== target.slipId.toString(),
      );
      this.syncStateToDisk();

      return this.policy.redactOutput(
        {
          mode: 'reclaimed',
          txHash: refunded.txHash,
          slipId: refunded.slipId.toString(),
          vault: refunded.vault,
          asset: refunded.asset,
          refundedAmountUnits: refunded.refundedAmountUnits.toString(),
          feeUnits: '0',
          transportTier: refunded.transportTier,
        },
        { allowedPublicHashFields: ['txHash'] },
      );
    }

    const refunded = await refundSlipDirect({
      publicClient: this.publicClient,
      slipId: input.slipId,
      vault: this.activeVault,
      ...(this.walletClient ? { walletClient: this.walletClient } : {}),
      paymasterSignerKey: this.operatorPrivateKey,
      useCirclePaymaster: !this.walletClient,
      bundlerUrls: this.transportOverrides.bundlerUrls,
      bundlerFetch: this.transportOverrides.bundlerFetch,
      mutex: this.mutex,
    });

    this.createdRevocableSlipIds = this.createdRevocableSlipIds.filter(
      (id) => id !== refunded.slipId.toString(),
    );
    this.syncStateToDisk();

    return this.policy.redactOutput(
      {
        mode: 'reclaimed',
        txHash: refunded.txHash,
        slipId: refunded.slipId.toString(),
        vault: refunded.vault,
        asset: refunded.asset,
        refundedAmountUnits: refunded.refundedAmountUnits.toString(),
        feeUnits: '0',
        transportTier: refunded.transportTier,
      },
      { allowedPublicHashFields: ['txHash'] },
    );
  }

  /**
   * Tool #7: `cryptoslip_withdraw_referrals` — Claims `0.25%` lifetime `referralCredits` on Base.
   */
  async withdrawReferrals(input?: {
    to?: string;
    assets?: readonly AnyAssetSymbol[];
  }): Promise<Record<string, unknown>> {
    await this.ensureBooted();

    const destination = input?.to
      ? this.policy.assertSafeDestination(input.to)
      : this.operatorAddress;

    const res = await withdrawReferralCredits({
      publicClient: this.publicClient,
      referrer: this.operatorAddress,
      to: destination,
      assets: input?.assets ?? ['USDC', 'cbBTC', 'ETH', 'NARA'],
      vault: this.activeVault,
      ...(this.walletClient ? { walletClient: this.walletClient } : {}),
      paymasterSignerKey: this.operatorPrivateKey,
      useCirclePaymaster: !this.walletClient,
      bundlerUrls: this.transportOverrides.bundlerUrls,
      bundlerFetch: this.transportOverrides.bundlerFetch,
    });

    const formattedWithdrawn: Record<string, string> = {};
    for (const [k, v] of Object.entries(res.withdrawnByAsset)) {
      if (v !== undefined) {
        formattedWithdrawn[k] = v.toString();
      }
    }

    return redactSecretsFromToolOutput(
      {
        vault: res.vault,
        referrer: res.referrer,
        to: res.to,
        withdrawnByAsset: formattedWithdrawn,
        txHashes: res.txHashes,
      },
      { allowedPublicHashFields: ['txHashes'] },
    );
  }
}
