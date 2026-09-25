#!/usr/bin/env node
import {
	candidateNextActions,
	coinCandidate,
	defaultLanguageCode,
	generateCandidate,
	readHealth,
	readLeaderboard,
	readStream,
	readWords,
	requireCandidateId,
	requireLanguageCode
} from '../src/runtime.mjs';

const [command = '', ...args] = process.argv.slice(2);
const printJson = value => console.log(JSON.stringify(value, null, 2));

function readLimit(value, fallback = 5) {
	if (value === undefined) return fallback;
	if (!/^\d{1,3}$/.test(value)) throw new Error('Limit must be an integer from 1 to 100.');
	const limit = Number(value);
	if (limit < 1 || limit > 100) throw new Error('Limit must be an integer from 1 to 100.');
	return limit;
}

async function publicRead(kind, limit) {
	const data = kind === 'leaderboard' ? await readLeaderboard(readLimit(limit)) : await readStream(readLimit(limit));
	printJson(data);
}

async function generate() {
	const languageArg = args.find(value => value.startsWith('--language='));
	const concept = args.filter(value => value !== languageArg).join(' ').trim();
	const languageCode = languageArg ? requireLanguageCode(languageArg.slice('--language='.length)) : defaultLanguageCode();
	const candidate = await generateCandidate(concept, languageCode);
	printJson({ ok: true, type: 'lingry.word_generated', candidate, reversible: true, coined: false, ...candidateNextActions() });
}

async function coin() {
	if (args.length !== 2 || args[1] !== '--publish') {
		throw new Error('Explicit publication action required: coin-word <candidate-id> --publish');
	}
	const candidateId = requireCandidateId(args[0]);
	const result = await coinCandidate(candidateId);
	printJson({ ok: true, type: 'lingry.word_coined', ...result, irreversible: true });
}

async function dailyWord() {
	const data = await readStream(20);
	const item = Array.isArray(data.items) ? data.items.find(value => value?.word && value?.meaning) : null;
	printJson({ ok: true, type: 'lingry.daily_word', word: item ? { word: item.word, part_of_speech: item.part_of_speech || '', meaning: item.meaning, txid: item.txid || '' } : null, read_only: true });
}

function usage() {
	console.log('Usage: lingry-agent [status] | doctor | stream [limit] | leaderboard [limit] | list-words [language] | daily-word | generate-word <concept> [--language=W] | prompt-another <concept> [--language=W] | coin-word <candidate-id> --publish');
}

async function main() {
	if (command === 'help' || command === '--help' || command === '-h') return usage();
	if (command === 'status' || command === 'doctor') {
		const health = await readHealth();
		return printJson({ ok: true, api_health: health, api_origin: 'https://lingry.net', local_state: false, local_credentials: false });
	}
	if (!command) return publicRead('stream', '1');
	if (command === 'stream' || command === 'leaderboard') return publicRead(command, args[0]);
	if (command === 'list-words') {
		const language = requireLanguageCode(args[0] || defaultLanguageCode());
		return printJson(await readWords(language));
	}
	if (command === 'daily-word') return dailyWord();
	if (command === 'generate-word' || command === 'prompt-another') return generate();
	if (command === 'coin-word') return coin();
	usage();
	process.exitCode = 1;
}

main().catch(error => { console.error(error.message || 'Lingry request failed.'); process.exitCode = 1; });
