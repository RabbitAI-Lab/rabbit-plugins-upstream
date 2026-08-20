import {
  pgTable,
  serial,
  text,
  timestamp,
  integer,
  boolean,
  varchar,
  jsonb,
} from "drizzle-orm/pg-core";

// Categories (I through X)
export const categories = pgTable("categories", {
  id: serial("id").primaryKey(),
  numeral: varchar("numeral", { length: 10 }).notNull(),
  name: text("name").notNull(),
  slug: varchar("slug", { length: 100 }).notNull().unique(),
  description: text("description"),
  sortOrder: integer("sort_order").notNull().default(0),
  createdAt: timestamp("created_at").defaultNow().notNull(),
});

// The 62 methods
export const methods = pgTable("methods", {
  id: serial("id").primaryKey(),
  categoryId: integer("category_id")
    .references(() => categories.id)
    .notNull(),
  methodNumber: integer("method_number").notNull().unique(),
  title: text("title").notNull(),
  description: text("description").notNull(),
  keywords: text("keywords").array(),
  createdAt: timestamp("created_at").defaultNow().notNull(),
});

// Curated resource sources
export const resources = pgTable("resources", {
  id: serial("id").primaryKey(),
  methodId: integer("method_id")
    .references(() => methods.id)
    .notNull(),
  title: text("title").notNull(),
  url: text("url").notNull(),
  source: varchar("source", { length: 200 }),
  resourceType: varchar("resource_type", { length: 50 }).notNull().default("article"),
  description: text("description"),
  createdAt: timestamp("created_at").defaultNow().notNull(),
});

// Indexed content from crawling
export const indexedContent = pgTable("indexed_content", {
  id: serial("id").primaryKey(),
  resourceId: integer("resource_id").references(() => resources.id),
  methodId: integer("method_id").references(() => methods.id),
  url: text("url").notNull(),
  title: text("title"),
  snippet: text("snippet"),
  fullContent: text("full_content"),
  relevanceScore: integer("relevance_score").default(0),
  lastCrawled: timestamp("last_crawled").defaultNow(),
  isCrawled: boolean("is_crawled").default(false),
  metadata: jsonb("metadata"),
  createdAt: timestamp("created_at").defaultNow().notNull(),
});

// Search history
export const searchHistory = pgTable("search_history", {
  id: serial("id").primaryKey(),
  query: text("query").notNull(),
  resultsCount: integer("results_count").default(0),
  categoryFilter: varchar("category_filter", { length: 100 }),
  createdAt: timestamp("created_at").defaultNow().notNull(),
});
