"use client";

import { useState, useEffect, useCallback, useRef } from "react";
import { 
  sanitizeSearchInput, 
  sanitizeUrl, 
  searchRateLimiter,
  debounce 
} from "@/lib/client-security";

// Types
interface Category {
  id: number;
  numeral: string;
  name: string;
  slug: string;
  description: string | null;
  sortOrder: number;
  methodCount: number;
}

interface Resource {
  id: number;
  methodId: number;
  title: string;
  url: string;
  source: string | null;
  resourceType: string;
  description: string | null;
}

interface SearchResult {
  methodId: number;
  methodNumber: number;
  title: string;
  description: string;
  keywords: string[] | null;
  categoryId: number;
  categoryName: string;
  categoryNumeral: string;
  categorySlug: string;
  resources: Resource[];
}

interface Stats {
  categories: number;
  methods: number;
  resources: number;
  totalSearches: number;
}

type ViewMode = "search" | "browse" | "method";

const CATEGORY_ICONS: Record<string, string> = {
  "mass-data-collection": "📡",
  "targeted-hacking": "🎯",
  "lotl-stealth": "👻",
  "hack-and-leak": "💧",
  "dos-disruption": "💥",
  "censorship-control": "🔒",
  "shutdowns-manipulation": "🔌",
  "domestic-surveillance": "👁️",
  "defensive-cyber": "🛡️",
  "intelligence-sharing": "🤝",
};

const RESOURCE_TYPE_COLORS: Record<string, string> = {
  government: "bg-blue-900/50 text-blue-300 border-blue-700",
  framework: "bg-purple-900/50 text-purple-300 border-purple-700",
  tool: "bg-green-900/50 text-green-300 border-green-700",
  academic: "bg-yellow-900/50 text-yellow-300 border-yellow-700",
  vendor: "bg-orange-900/50 text-orange-300 border-orange-700",
  advocacy: "bg-red-900/50 text-red-300 border-red-700",
  organization: "bg-cyan-900/50 text-cyan-300 border-cyan-700",
  standard: "bg-indigo-900/50 text-indigo-300 border-indigo-700",
  education: "bg-teal-900/50 text-teal-300 border-teal-700",
  blog: "bg-pink-900/50 text-pink-300 border-pink-700",
  research: "bg-amber-900/50 text-amber-300 border-amber-700",
  article: "bg-gray-700/50 text-gray-300 border-gray-600",
};

// Allowed slug characters (security)
const VALID_SLUG_REGEX = /^[a-z0-9-]+$/;

function isValidSlug(slug: string): boolean {
  return VALID_SLUG_REGEX.test(slug) && slug.length <= 100;
}

export default function SearchEngine() {
  const [query, setQuery] = useState("");
  const [results, setResults] = useState<SearchResult[]>([]);
  const [categories, setCategories] = useState<Category[]>([]);
  const [selectedCategory, setSelectedCategory] = useState("");
  const [isLoading, setIsLoading] = useState(false);
  const [isSeeded, setIsSeeded] = useState(false);
  const [isSeeding, setIsSeeding] = useState(false);
  const [stats, setStats] = useState<Stats | null>(null);
  const [viewMode, setViewMode] = useState<ViewMode>("search");
  const [selectedMethod, setSelectedMethod] = useState<SearchResult | null>(null);
  const [totalResults, setTotalResults] = useState(0);
  const [currentPage, setCurrentPage] = useState(1);
  const [totalPages, setTotalPages] = useState(1);
  const [expandedResults, setExpandedResults] = useState<Set<number>>(new Set());
  const searchInputRef = useRef<HTMLInputElement>(null);
  const [hasSearched, setHasSearched] = useState(false);
  const [error, setError] = useState<string | null>(null);

  // Secure fetch wrapper with error handling
  const secureFetch = useCallback(async (url: string, options?: RequestInit) => {
    try {
      const controller = new AbortController();
      const timeoutId = setTimeout(() => controller.abort(), 30000); // 30s timeout

      const response = await fetch(url, {
        ...options,
        signal: controller.signal,
        headers: {
          "Content-Type": "application/json",
          ...options?.headers,
        },
      });

      clearTimeout(timeoutId);

      if (!response.ok) {
        if (response.status === 429) {
          throw new Error("Rate limit exceeded. Please wait a moment.");
        }
        throw new Error(`Request failed: ${response.status}`);
      }

      return response;
    } catch (err) {
      if (err instanceof Error) {
        if (err.name === "AbortError") {
          throw new Error("Request timeout. Please try again.");
        }
        throw err;
      }
      throw new Error("An unknown error occurred");
    }
  }, []);

  // Seed the database on first load
  useEffect(() => {
    async function init() {
      try {
        setIsSeeding(true);
        setError(null);
        
        const seedRes = await secureFetch("/api/seed", { method: "POST" });
        await seedRes.json();
        setIsSeeded(true);

        // Load categories
        const catRes = await secureFetch("/api/categories");
        const catData = await catRes.json();
        setCategories(catData.categories || []);

        // Load stats
        const statsRes = await secureFetch("/api/stats");
        const statsData = await statsRes.json();
        setStats(statsData.stats || null);
      } catch (err) {
        console.error("Init error:", err);
        setError(err instanceof Error ? err.message : "Initialization failed");
      } finally {
        setIsSeeding(false);
      }
    }
    init();
  }, [secureFetch]);

  // Search function with security measures
  const performSearch = useCallback(
    async (searchQuery: string, category: string, page: number = 1) => {
      // Client-side rate limiting
      if (!searchRateLimiter.canMakeRequest()) {
        setError("Please slow down your searches");
        return;
      }

      // Sanitize inputs
      const sanitizedQuery = sanitizeSearchInput(searchQuery);
      const sanitizedCategory = category && isValidSlug(category) ? category : "";

      if (!sanitizedQuery && !sanitizedCategory) {
        setResults([]);
        setHasSearched(false);
        return;
      }

      setIsLoading(true);
      setHasSearched(true);
      setError(null);

      try {
        const params = new URLSearchParams();
        if (sanitizedQuery) params.set("q", sanitizedQuery);
        if (sanitizedCategory) params.set("category", sanitizedCategory);
        params.set("page", String(Math.max(1, Math.min(page, 1000))));
        params.set("limit", "20");

        const res = await secureFetch(`/api/search?${params.toString()}`);
        const data = await res.json();

        setResults(data.results || []);
        setTotalResults(data.total || 0);
        setCurrentPage(data.page || 1);
        setTotalPages(data.totalPages || 1);
      } catch (err) {
        console.error("Search error:", err);
        setError(err instanceof Error ? err.message : "Search failed");
        setResults([]);
      } finally {
        setIsLoading(false);
      }
    },
    [secureFetch]
  );

  // Browse category methods
  const browseCategory = useCallback(async (slug: string) => {
    // Validate slug
    if (!isValidSlug(slug)) {
      setError("Invalid category");
      return;
    }

    setIsLoading(true);
    setViewMode("browse");
    setSelectedCategory(slug);
    setError(null);

    try {
      const res = await secureFetch(`/api/methods?category=${encodeURIComponent(slug)}`);
      const data = await res.json();
      setResults(data.methods || []);
      setTotalResults(data.methods?.length || 0);
    } catch (err) {
      console.error("Browse error:", err);
      setError(err instanceof Error ? err.message : "Failed to load methods");
    } finally {
      setIsLoading(false);
    }
  }, [secureFetch]);

  // View all methods
  const browseAll = useCallback(async () => {
    setIsLoading(true);
    setViewMode("browse");
    setSelectedCategory("");
    setError(null);

    try {
      const res = await secureFetch("/api/methods");
      const data = await res.json();
      setResults(data.methods || []);
      setTotalResults(data.methods?.length || 0);
    } catch (err) {
      console.error("Browse all error:", err);
      setError(err instanceof Error ? err.message : "Failed to load methods");
    } finally {
      setIsLoading(false);
    }
  }, [secureFetch]);

  const handleSearch = (e: React.FormEvent) => {
    e.preventDefault();
    setViewMode("search");
    performSearch(query, selectedCategory);
  };

  const handleCategoryFilter = (slug: string) => {
    if (!isValidSlug(slug)) return;
    
    if (viewMode === "search") {
      const newCat = selectedCategory === slug ? "" : slug;
      setSelectedCategory(newCat);
      if (query || newCat) {
        performSearch(query, newCat);
      }
    } else {
      browseCategory(slug);
    }
  };

  const toggleExpanded = (methodId: number) => {
    if (typeof methodId !== "number" || methodId < 0) return;
    
    setExpandedResults((prev) => {
      const next = new Set(prev);
      if (next.has(methodId)) {
        next.delete(methodId);
      } else {
        next.add(methodId);
      }
      return next;
    });
  };

  const viewMethodDetail = (method: SearchResult) => {
    setSelectedMethod(method);
    setViewMode("method");
  };

  const goBack = () => {
    setSelectedMethod(null);
    setViewMode("search");
  };

  // Loading/seeding screen
  if (isSeeding) {
    return (
      <div className="min-h-screen flex items-center justify-center bg-gray-950 grid-bg">
        <div className="text-center">
          <div className="inline-block w-16 h-16 border-4 border-emerald-500/30 border-t-emerald-400 rounded-full animate-spin mb-6"></div>
          <h2 className="text-2xl font-bold text-emerald-400 mb-2">Initializing CyberScope</h2>
          <p className="text-gray-400">Seeding database with 62 cyber methods &amp; resources...</p>
        </div>
      </div>
    );
  }

  return (
    <div className="min-h-screen bg-gray-950 grid-bg">
      {/* Header */}
      <header className="sticky top-0 z-50 bg-gray-950/90 backdrop-blur-xl border-b border-gray-800">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="flex items-center justify-between h-16">
            <button
              onClick={() => {
                setViewMode("search");
                setQuery("");
                setSelectedCategory("");
                setResults([]);
                setHasSearched(false);
                setSelectedMethod(null);
                setError(null);
              }}
              className="flex items-center gap-3 hover:opacity-80 transition-opacity"
            >
              <div className="w-9 h-9 rounded-lg bg-gradient-to-br from-emerald-500 to-cyan-500 flex items-center justify-center pulse-glow">
                <svg className="w-5 h-5 text-white" fill="none" viewBox="0 0 24 24" stroke="currentColor" strokeWidth={2.5}>
                  <path strokeLinecap="round" strokeLinejoin="round" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z" />
                </svg>
              </div>
              <div>
                <h1 className="text-lg font-bold bg-gradient-to-r from-emerald-400 to-cyan-400 bg-clip-text text-transparent">
                  CyberScope
                </h1>
                <p className="text-[10px] text-gray-500 -mt-0.5 tracking-wider uppercase">Hardened Search Engine</p>
              </div>
            </button>

            <nav className="hidden sm:flex items-center gap-1">
              <button
                onClick={() => {
                  setViewMode("search");
                  setSelectedMethod(null);
                  searchInputRef.current?.focus();
                }}
                className={`px-3 py-1.5 rounded-lg text-sm font-medium transition-colors ${
                  viewMode === "search"
                    ? "bg-emerald-500/20 text-emerald-400"
                    : "text-gray-400 hover:text-gray-200 hover:bg-gray-800"
                }`}
              >
                🔍 Search
              </button>
              <button
                onClick={browseAll}
                className={`px-3 py-1.5 rounded-lg text-sm font-medium transition-colors ${
                  viewMode === "browse"
                    ? "bg-emerald-500/20 text-emerald-400"
                    : "text-gray-400 hover:text-gray-200 hover:bg-gray-800"
                }`}
              >
                📂 Browse All
              </button>
            </nav>

            {stats && (
              <div className="hidden md:flex items-center gap-4 text-xs text-gray-500">
                <span><strong className="text-emerald-400">{stats.methods}</strong> methods</span>
                <span><strong className="text-cyan-400">{stats.resources}</strong> resources</span>
                <span className="px-2 py-0.5 bg-emerald-500/10 border border-emerald-500/30 rounded text-emerald-400">🔒 Hardened</span>
              </div>
            )}
          </div>
        </div>
      </header>

      <main className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-6">
        {/* Error Banner */}
        {error && (
          <div className="mb-6 p-4 bg-red-900/20 border border-red-500/30 rounded-xl">
            <div className="flex items-center gap-3">
              <svg className="w-5 h-5 text-red-400 flex-shrink-0" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z" />
              </svg>
              <p className="text-red-400 text-sm">{error}</p>
              <button 
                onClick={() => setError(null)}
                className="ml-auto text-red-400 hover:text-red-300"
              >
                ✕
              </button>
            </div>
          </div>
        )}

        {/* Method Detail View */}
        {viewMode === "method" && selectedMethod && (
          <MethodDetail method={selectedMethod} onBack={goBack} />
        )}

        {/* Search View */}
        {viewMode !== "method" && (
          <>
            {/* Hero / Search Bar */}
            {!hasSearched && viewMode === "search" && (
              <div className="text-center py-12 sm:py-20">
                <div className="inline-block mb-6">
                  <div className="w-20 h-20 mx-auto rounded-2xl bg-gradient-to-br from-emerald-500/20 to-cyan-500/20 border border-emerald-500/30 flex items-center justify-center pulse-glow">
                    <svg className="w-10 h-10 text-emerald-400" fill="none" viewBox="0 0 24 24" stroke="currentColor" strokeWidth={1.5}>
                      <path strokeLinecap="round" strokeLinejoin="round" d="M9 12.75L11.25 15 15 9.75m-3-7.036A11.959 11.959 0 013.598 6 11.99 11.99 0 003 9.749c0 5.592 3.824 10.29 9 11.623 5.176-1.332 9-6.03 9-11.622 0-1.31-.21-2.571-.598-3.751h-.152c-3.196 0-6.1-1.248-8.25-3.285z" />
                    </svg>
                  </div>
                </div>
                <h2 className="text-3xl sm:text-5xl font-bold mb-4">
                  <span className="bg-gradient-to-r from-emerald-400 via-cyan-400 to-purple-400 bg-clip-text text-transparent">
                    CyberScope
                  </span>
                </h2>
                <p className="text-gray-400 text-base sm:text-lg max-w-2xl mx-auto mb-2">
                  Security-Hardened Search Engine for Internet Data Leak Prevention, Surveillance,
                  Censorship &amp; Cyber Operations Methods
                </p>
                <p className="text-gray-600 text-sm mb-8">
                  62 documented techniques • 10 categories • 100+ curated resources • 🔒 Hardened Security
                </p>
              </div>
            )}

            {/* Search Form */}
            <form onSubmit={handleSearch} className={`max-w-3xl mx-auto ${hasSearched || viewMode === "browse" ? "mb-6" : "mb-12"}`}>
              <div className="relative">
                <div className="absolute inset-y-0 left-0 pl-4 flex items-center pointer-events-none">
                  <svg className="w-5 h-5 text-gray-500" fill="none" viewBox="0 0 24 24" stroke="currentColor" strokeWidth={2}>
                    <path strokeLinecap="round" strokeLinejoin="round" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z" />
                  </svg>
                </div>
                <input
                  ref={searchInputRef}
                  type="text"
                  value={query}
                  onChange={(e) => setQuery(sanitizeSearchInput(e.target.value))}
                  placeholder="Search cyber operations methods, techniques, tools..."
                  maxLength={200}
                  autoComplete="off"
                  spellCheck={false}
                  className="w-full pl-12 pr-32 py-4 bg-gray-900 border border-gray-700 rounded-xl text-gray-100 placeholder-gray-500 focus:outline-none focus:border-emerald-500 focus:ring-2 focus:ring-emerald-500/20 text-base"
                />
                <div className="absolute inset-y-0 right-0 flex items-center pr-2">
                  <button
                    type="submit"
                    className="px-5 py-2 bg-gradient-to-r from-emerald-600 to-cyan-600 hover:from-emerald-500 hover:to-cyan-500 text-white font-medium rounded-lg transition-all duration-200 text-sm"
                  >
                    Search
                  </button>
                </div>
              </div>

              {/* Quick suggestion chips */}
              {!hasSearched && viewMode === "search" && (
                <div className="mt-4 flex flex-wrap gap-2 justify-center">
                  {["DDoS", "phishing", "VPN blocking", "supply chain", "ransomware", "DPI", "insider threat", "zero-day"].map(
                    (chip) => (
                      <button
                        key={chip}
                        type="button"
                        onClick={() => {
                          const sanitized = sanitizeSearchInput(chip);
                          setQuery(sanitized);
                          setViewMode("search");
                          performSearch(sanitized, selectedCategory);
                        }}
                        className="px-3 py-1 text-xs rounded-full border border-gray-700 text-gray-400 hover:border-emerald-500/50 hover:text-emerald-400 hover:bg-emerald-500/10 transition-all"
                      >
                        {chip}
                      </button>
                    )
                  )}
                </div>
              )}
            </form>

            {/* Category Pills */}
            <div className="mb-6 overflow-x-auto">
              <div className="flex gap-2 pb-2 min-w-max">
                {viewMode === "browse" && (
                  <button
                    onClick={browseAll}
                    className={`px-3 py-1.5 rounded-full text-xs font-medium border whitespace-nowrap transition-all ${
                      !selectedCategory
                        ? "bg-emerald-500/20 border-emerald-500/50 text-emerald-400"
                        : "border-gray-700 text-gray-400 hover:border-gray-500"
                    }`}
                  >
                    All Methods
                  </button>
                )}
                {categories.map((cat) => (
                  <button
                    key={cat.slug}
                    onClick={() => handleCategoryFilter(cat.slug)}
                    className={`px-3 py-1.5 rounded-full text-xs font-medium border whitespace-nowrap transition-all ${
                      selectedCategory === cat.slug
                        ? "bg-emerald-500/20 border-emerald-500/50 text-emerald-400"
                        : "border-gray-700 text-gray-400 hover:border-gray-500"
                    }`}
                  >
                    {CATEGORY_ICONS[cat.slug] || "📁"} {cat.numeral}. {cat.name}
                    <span className="ml-1 text-gray-600">({cat.methodCount})</span>
                  </button>
                ))}
              </div>
            </div>

            {/* Results Count */}
            {(hasSearched || viewMode === "browse") && !isLoading && (
              <div className="mb-4 flex items-center justify-between">
                <p className="text-sm text-gray-400">
                  {totalResults > 0 ? (
                    <>
                      Found <strong className="text-emerald-400">{totalResults}</strong> result{totalResults !== 1 ? "s" : ""}
                      {query && <> for &quot;<span className="text-cyan-400">{query}</span>&quot;</>}
                      {selectedCategory && (
                        <>
                          {" "}in{" "}
                          <span className="text-purple-400">
                            {categories.find((c) => c.slug === selectedCategory)?.name}
                          </span>
                        </>
                      )}
                    </>
                  ) : (
                    hasSearched && "No results found. Try a different query or category."
                  )}
                </p>
                {results.length > 0 && (
                  <button
                    onClick={() => {
                      if (expandedResults.size > 0) {
                        setExpandedResults(new Set());
                      } else {
                        setExpandedResults(new Set(results.map((r) => r.methodId)));
                      }
                    }}
                    className="text-xs text-gray-500 hover:text-gray-300 transition-colors"
                  >
                    {expandedResults.size > 0 ? "Collapse All" : "Expand All"}
                  </button>
                )}
              </div>
            )}

            {/* Loading Indicator */}
            {isLoading && (
              <div className="flex justify-center py-12">
                <div className="flex items-center gap-3 text-emerald-400">
                  <div className="w-5 h-5 border-2 border-emerald-500/30 border-t-emerald-400 rounded-full animate-spin"></div>
                  <span className="text-sm">Scanning resources...</span>
                </div>
              </div>
            )}

            {/* Results Grid */}
            {!isLoading && results.length > 0 && (
              <div className="space-y-3">
                {results.map((result) => (
                  <ResultCard
                    key={result.methodId}
                    result={result}
                    isExpanded={expandedResults.has(result.methodId)}
                    onToggle={() => toggleExpanded(result.methodId)}
                    onViewDetail={() => viewMethodDetail(result)}
                    searchQuery={query}
                  />
                ))}
              </div>
            )}

            {/* Category Cards (on home page) */}
            {!hasSearched && viewMode === "search" && categories.length > 0 && (
              <div className="mt-8">
                <h3 className="text-lg font-semibold text-gray-300 mb-4 flex items-center gap-2">
                  <span className="w-1 h-5 bg-gradient-to-b from-emerald-500 to-cyan-500 rounded-full"></span>
                  Browse by Category
                </h3>
                <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-5 gap-3">
                  {categories.map((cat) => (
                    <button
                      key={cat.slug}
                      onClick={() => browseCategory(cat.slug)}
                      className="group p-4 bg-gray-900/50 border border-gray-800 rounded-xl hover:border-emerald-500/30 hover:bg-gray-900 transition-all text-left"
                    >
                      <div className="text-2xl mb-2">{CATEGORY_ICONS[cat.slug] || "📁"}</div>
                      <div className="text-xs text-emerald-500/70 font-mono mb-1">{cat.numeral}</div>
                      <h4 className="text-sm font-semibold text-gray-200 group-hover:text-emerald-400 transition-colors leading-tight mb-1">
                        {cat.name}
                      </h4>
                      <p className="text-xs text-gray-500">
                        {cat.methodCount} method{cat.methodCount !== 1 ? "s" : ""}
                      </p>
                    </button>
                  ))}
                </div>
              </div>
            )}
          </>
        )}
      </main>

      {/* Footer */}
      <footer className="border-t border-gray-800 mt-12">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-6">
          <div className="flex flex-col sm:flex-row items-center justify-between gap-4 text-xs text-gray-600">
            <p>CyberScope — Security-Hardened Cyber Operations Search Engine</p>
            <div className="flex items-center gap-2">
              <span className="px-2 py-0.5 bg-emerald-500/10 border border-emerald-500/30 rounded text-emerald-500">🔒 CSP</span>
              <span className="px-2 py-0.5 bg-cyan-500/10 border border-cyan-500/30 rounded text-cyan-500">🛡️ Rate Limited</span>
              <span className="px-2 py-0.5 bg-purple-500/10 border border-purple-500/30 rounded text-purple-500">✓ Input Validated</span>
            </div>
          </div>
        </div>
      </footer>
    </div>
  );
}

// Result Card Component
function ResultCard({
  result,
  isExpanded,
  onToggle,
  onViewDetail,
  searchQuery,
}: {
  result: SearchResult;
  isExpanded: boolean;
  onToggle: () => void;
  onViewDetail: () => void;
  searchQuery: string;
}) {
  const highlightText = (text: string, query: string) => {
    if (!query) return text;
    // Escape regex special characters for safety
    const escaped = query.replace(/[.*+?^${}()|[\]\\]/g, "\\$&");
    const regex = new RegExp(`(${escaped})`, "gi");
    const parts = text.split(regex);
    return parts.map((part, i) =>
      regex.test(part) ? (
        <mark key={i} className="bg-emerald-500/30 text-emerald-300 rounded px-0.5">
          {part}
        </mark>
      ) : (
        part
      )
    );
  };

  return (
    <div className="group bg-gray-900/50 border border-gray-800 rounded-xl hover:border-gray-700 transition-all overflow-hidden">
      {/* Main Row */}
      <div className="p-4 flex items-start gap-4 cursor-pointer" onClick={onToggle}>
        {/* Method Number */}
        <div className="flex-shrink-0 w-10 h-10 rounded-lg bg-gradient-to-br from-emerald-500/20 to-cyan-500/20 border border-emerald-500/20 flex items-center justify-center">
          <span className="text-sm font-bold text-emerald-400">{result.methodNumber}</span>
        </div>

        {/* Content */}
        <div className="flex-1 min-w-0">
          <div className="flex items-center gap-2 mb-1 flex-wrap">
            <span className="text-[10px] font-mono px-1.5 py-0.5 rounded bg-gray-800 text-gray-400">
              {CATEGORY_ICONS[result.categorySlug] || "📁"} {result.categoryNumeral}
            </span>
            <span className="text-[10px] text-gray-600">{result.categoryName}</span>
          </div>
          <h3 className="text-base font-semibold text-gray-100 group-hover:text-emerald-400 transition-colors">
            {highlightText(result.title, searchQuery)}
          </h3>
          <p className="text-sm text-gray-400 mt-1 line-clamp-2">
            {highlightText(result.description, searchQuery)}
          </p>
          {/* Keywords */}
          {result.keywords && result.keywords.length > 0 && (
            <div className="flex flex-wrap gap-1 mt-2">
              {result.keywords.slice(0, 6).map((kw) => (
                <span
                  key={kw}
                  className="px-1.5 py-0.5 text-[10px] rounded bg-gray-800/80 text-gray-500 border border-gray-700/50"
                >
                  {kw}
                </span>
              ))}
            </div>
          )}
        </div>

        {/* Expand indicator */}
        <div className="flex-shrink-0 flex items-center gap-2">
          <span className="text-[10px] text-gray-600">
            {result.resources.length} source{result.resources.length !== 1 ? "s" : ""}
          </span>
          <svg
            className={`w-4 h-4 text-gray-500 transition-transform duration-200 ${isExpanded ? "rotate-180" : ""}`}
            fill="none"
            viewBox="0 0 24 24"
            stroke="currentColor"
            strokeWidth={2}
          >
            <path strokeLinecap="round" strokeLinejoin="round" d="M19 9l-7 7-7-7" />
          </svg>
        </div>
      </div>

      {/* Expanded Resources */}
      {isExpanded && (
        <div className="border-t border-gray-800 bg-gray-950/50 p-4">
          <div className="flex items-center justify-between mb-3">
            <h4 className="text-xs font-semibold text-gray-400 uppercase tracking-wider">
              Curated Resources &amp; Sources
            </h4>
            <button
              onClick={(e) => {
                e.stopPropagation();
                onViewDetail();
              }}
              className="text-xs text-emerald-400 hover:text-emerald-300 transition-colors"
            >
              Full Details →
            </button>
          </div>
          {result.resources.length > 0 ? (
            <div className="space-y-2">
              {result.resources.map((resource) => (
                <a
                  key={resource.id}
                  href={sanitizeUrl(resource.url)}
                  target="_blank"
                  rel="noopener noreferrer"
                  onClick={(e) => e.stopPropagation()}
                  className="flex items-start gap-3 p-3 rounded-lg bg-gray-900/50 border border-gray-800 hover:border-emerald-500/30 hover:bg-gray-900 transition-all group/link"
                >
                  <div className="flex-shrink-0 mt-0.5">
                    <svg className="w-4 h-4 text-gray-600 group-hover/link:text-emerald-400 transition-colors" fill="none" viewBox="0 0 24 24" stroke="currentColor" strokeWidth={2}>
                      <path strokeLinecap="round" strokeLinejoin="round" d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14" />
                    </svg>
                  </div>
                  <div className="flex-1 min-w-0">
                    <div className="flex items-center gap-2 mb-0.5">
                      <span className="text-sm font-medium text-gray-200 group-hover/link:text-emerald-400 transition-colors">
                        {resource.title}
                      </span>
                      <span
                        className={`px-1.5 py-0.5 text-[9px] font-medium rounded border ${
                          RESOURCE_TYPE_COLORS[resource.resourceType] || RESOURCE_TYPE_COLORS.article
                        }`}
                      >
                        {resource.resourceType}
                      </span>
                    </div>
                    <p className="text-xs text-gray-500 truncate">{resource.url}</p>
                    {resource.description && (
                      <p className="text-xs text-gray-400 mt-1">{resource.description}</p>
                    )}
                    {resource.source && (
                      <span className="text-[10px] text-gray-600 mt-1 inline-block">
                        Source: {resource.source}
                      </span>
                    )}
                  </div>
                </a>
              ))}
            </div>
          ) : (
            <p className="text-sm text-gray-600 italic">No resources available for this method.</p>
          )}
        </div>
      )}
    </div>
  );
}

// Method Detail Component
function MethodDetail({ method, onBack }: { method: SearchResult; onBack: () => void }) {
  return (
    <div>
      {/* Breadcrumb */}
      <div className="flex items-center gap-2 mb-6 text-sm">
        <button onClick={onBack} className="text-gray-400 hover:text-emerald-400 transition-colors flex items-center gap-1">
          <svg className="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor" strokeWidth={2}>
            <path strokeLinecap="round" strokeLinejoin="round" d="M15 19l-7-7 7-7" />
          </svg>
          Back
        </button>
        <span className="text-gray-700">/</span>
        <span className="text-gray-500">{method.categoryName}</span>
        <span className="text-gray-700">/</span>
        <span className="text-emerald-400">Method #{method.methodNumber}</span>
      </div>

      {/* Method Header */}
      <div className="bg-gray-900/50 border border-gray-800 rounded-2xl p-6 sm:p-8 mb-6">
        <div className="flex items-start gap-4 mb-6">
          <div className="w-14 h-14 rounded-xl bg-gradient-to-br from-emerald-500/20 to-cyan-500/20 border border-emerald-500/20 flex items-center justify-center flex-shrink-0">
            <span className="text-xl font-bold text-emerald-400">{method.methodNumber}</span>
          </div>
          <div>
            <div className="flex items-center gap-2 mb-2">
              <span className="px-2 py-1 text-xs rounded-full bg-gray-800 text-gray-400 border border-gray-700">
                {CATEGORY_ICONS[method.categorySlug]} {method.categoryNumeral}. {method.categoryName}
              </span>
            </div>
            <h1 className="text-2xl sm:text-3xl font-bold text-gray-100">{method.title}</h1>
          </div>
        </div>

        <div className="bg-gray-950/50 rounded-xl p-4 mb-6">
          <h3 className="text-xs font-semibold text-gray-500 uppercase tracking-wider mb-2">Description</h3>
          <p className="text-gray-300 leading-relaxed">{method.description}</p>
        </div>

        {method.keywords && method.keywords.length > 0 && (
          <div>
            <h3 className="text-xs font-semibold text-gray-500 uppercase tracking-wider mb-2">Keywords</h3>
            <div className="flex flex-wrap gap-2">
              {method.keywords.map((kw) => (
                <span
                  key={kw}
                  className="px-2.5 py-1 text-xs rounded-lg bg-emerald-500/10 text-emerald-400 border border-emerald-500/20"
                >
                  {kw}
                </span>
              ))}
            </div>
          </div>
        )}
      </div>

      {/* Resources */}
      <div className="bg-gray-900/50 border border-gray-800 rounded-2xl p-6 sm:p-8">
        <h2 className="text-lg font-semibold text-gray-200 mb-1 flex items-center gap-2">
          <span className="w-1 h-5 bg-gradient-to-b from-emerald-500 to-cyan-500 rounded-full"></span>
          Curated Resources &amp; Sources
        </h2>
        <p className="text-xs text-gray-500 mb-6">
          {method.resources.length} authoritative source{method.resources.length !== 1 ? "s" : ""} for this method
        </p>

        {method.resources.length > 0 ? (
          <div className="grid gap-3">
            {method.resources.map((resource) => (
              <a
                key={resource.id}
                href={sanitizeUrl(resource.url)}
                target="_blank"
                rel="noopener noreferrer"
                className="flex items-start gap-4 p-4 rounded-xl bg-gray-950/50 border border-gray-800 hover:border-emerald-500/30 hover:bg-gray-900 transition-all group"
              >
                <div className="flex-shrink-0 w-10 h-10 rounded-lg bg-gray-800 flex items-center justify-center group-hover:bg-emerald-500/20 transition-colors">
                  <svg className="w-5 h-5 text-gray-500 group-hover:text-emerald-400 transition-colors" fill="none" viewBox="0 0 24 24" stroke="currentColor" strokeWidth={2}>
                    <path strokeLinecap="round" strokeLinejoin="round" d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14" />
                  </svg>
                </div>
                <div className="flex-1 min-w-0">
                  <div className="flex items-center gap-2 mb-1 flex-wrap">
                    <span className="text-sm font-semibold text-gray-200 group-hover:text-emerald-400 transition-colors">
                      {resource.title}
                    </span>
                    <span
                      className={`px-1.5 py-0.5 text-[9px] font-medium rounded border ${
                        RESOURCE_TYPE_COLORS[resource.resourceType] || RESOURCE_TYPE_COLORS.article
                      }`}
                    >
                      {resource.resourceType}
                    </span>
                  </div>
                  <p className="text-xs text-emerald-500/70 truncate mb-1">{resource.url}</p>
                  {resource.description && (
                    <p className="text-sm text-gray-400">{resource.description}</p>
                  )}
                  {resource.source && (
                    <p className="text-xs text-gray-600 mt-2">Source: {resource.source}</p>
                  )}
                </div>
                <svg className="w-4 h-4 text-gray-700 group-hover:text-emerald-400 transition-colors flex-shrink-0 mt-2" fill="none" viewBox="0 0 24 24" stroke="currentColor" strokeWidth={2}>
                  <path strokeLinecap="round" strokeLinejoin="round" d="M9 5l7 7-7 7" />
                </svg>
              </a>
            ))}
          </div>
        ) : (
          <div className="text-center py-8">
            <p className="text-gray-500">No curated resources available for this method yet.</p>
          </div>
        )}
      </div>
    </div>
  );
}
