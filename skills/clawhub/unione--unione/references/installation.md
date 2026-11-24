# Install a UniOne SDK or framework package

Every package reads the API key from `UNIONE_API_KEY` and has an `AGENTS.md` with the integration rules. Prefer the framework package when the project uses that framework: it brings the SDK, configuration, the mailer and the webhook endpoint. Two lines of a language (PHP 8.1 / 7.2, Node.js 18 / 14, Java 11 / 8, .NET 8 / Standard 2.0) are two major versions of one package. Composer picks the line by the PHP version; npm, NuGet and Maven install the newest major whatever the runtime, so the old line names its major as below (npm `@1`, NuGet `--version 1.*`; Maven / Gradle pin the exact 1.x version shown).

## SDKs

### PHP — PHP 8.1+

```bash
composer require unione-repo/unione-php-sdk
```

[github.com/unione-repo/unione-php-sdk](https://github.com/unione-repo/unione-php-sdk), [AGENTS.md](https://github.com/unione-repo/unione-php-sdk/blob/HEAD/AGENTS.md)

### PHP — PHP 7.2+

```bash
composer require unione-repo/unione-php-sdk
```

[github.com/unione-repo/unione-php-sdk](https://github.com/unione-repo/unione-php-sdk), [AGENTS.md](https://github.com/unione-repo/unione-php-sdk/blob/HEAD/AGENTS.md)

### Python — Python 3.8+

```bash
pip install unione-sdk
```

[github.com/unione-repo/unione-python-sdk](https://github.com/unione-repo/unione-python-sdk), [AGENTS.md](https://github.com/unione-repo/unione-python-sdk/blob/HEAD/AGENTS.md)

### Node.js — Node.js 18+

```bash
npm install unione
```

[github.com/unione-repo/unione-node-sdk](https://github.com/unione-repo/unione-node-sdk), [AGENTS.md](https://github.com/unione-repo/unione-node-sdk/blob/HEAD/AGENTS.md)

### Node.js — Node.js 14+

```bash
npm install unione@1
```

[github.com/unione-repo/unione-node-sdk](https://github.com/unione-repo/unione-node-sdk), [AGENTS.md](https://github.com/unione-repo/unione-node-sdk/blob/HEAD/AGENTS.md)

### Ruby — Ruby 2.7+

```bash
gem install unione
```

[github.com/unione-repo/unione-ruby-sdk](https://github.com/unione-repo/unione-ruby-sdk), [AGENTS.md](https://github.com/unione-repo/unione-ruby-sdk/blob/HEAD/AGENTS.md)

### Go — Go 1.18+

```bash
go get github.com/unione-repo/unione-go-sdk
```

[github.com/unione-repo/unione-go-sdk](https://github.com/unione-repo/unione-go-sdk), [AGENTS.md](https://github.com/unione-repo/unione-go-sdk/blob/HEAD/AGENTS.md)

### Java — Java 11+

```xml
<dependency>
    <groupId>io.unione</groupId>
    <artifactId>unione-java-sdk</artifactId>
    <version>2.3.1</version>
</dependency>
```

[github.com/unione-repo/unione-java-sdk](https://github.com/unione-repo/unione-java-sdk), [AGENTS.md](https://github.com/unione-repo/unione-java-sdk/blob/HEAD/AGENTS.md)

### Java — Java 8+

```xml
<dependency>
    <groupId>io.unione</groupId>
    <artifactId>unione-java-sdk</artifactId>
    <version>1.3.1</version>
</dependency>
```

[github.com/unione-repo/unione-java-sdk](https://github.com/unione-repo/unione-java-sdk), [AGENTS.md](https://github.com/unione-repo/unione-java-sdk/blob/HEAD/AGENTS.md)

### .NET (C#) — .NET 8

```bash
dotnet add package UniOne
```

[github.com/unione-repo/unione-dotnet-sdk](https://github.com/unione-repo/unione-dotnet-sdk), [AGENTS.md](https://github.com/unione-repo/unione-dotnet-sdk/blob/HEAD/AGENTS.md)

### .NET (C#) — .NET Standard 2.0 (.NET Framework 4.6.2+, .NET 6+)

```bash
dotnet add package UniOne --version 1.*
```

[github.com/unione-repo/unione-dotnet-sdk](https://github.com/unione-repo/unione-dotnet-sdk), [AGENTS.md](https://github.com/unione-repo/unione-dotnet-sdk/blob/HEAD/AGENTS.md)

### Rust — Rust 1.70+ (edition 2021), async runtime (tokio)

```bash
cargo add unione-rust-sdk
cargo add tokio --features macros,rt-multi-thread
```

[github.com/unione-repo/unione-rust-sdk](https://github.com/unione-repo/unione-rust-sdk), [AGENTS.md](https://github.com/unione-repo/unione-rust-sdk/blob/HEAD/AGENTS.md)

## Framework packages

### Laravel — `unione-repo/unione-laravel`

```bash
composer require unione-repo/unione-laravel
php artisan unione:install  # config/unione.php, UNIONE_API_KEY in .env
```

[github.com/unione-repo/unione-laravel](https://github.com/unione-repo/unione-laravel), [AGENTS.md](https://github.com/unione-repo/unione-laravel/blob/HEAD/AGENTS.md)

### Symfony — `unione-repo/unione-symfony-bundle`

```bash
composer require unione-repo/unione-symfony-bundle
```

[github.com/unione-repo/unione-symfony](https://github.com/unione-repo/unione-symfony), [AGENTS.md](https://github.com/unione-repo/unione-symfony/blob/HEAD/AGENTS.md)

### Django — `unione-django`

```bash
pip install unione-django
```

[github.com/unione-repo/unione-django](https://github.com/unione-repo/unione-django), [AGENTS.md](https://github.com/unione-repo/unione-django/blob/HEAD/AGENTS.md)

### Flask — `unione-flask`

```bash
pip install unione-flask
```

[github.com/unione-repo/unione-flask](https://github.com/unione-repo/unione-flask), [AGENTS.md](https://github.com/unione-repo/unione-flask/blob/HEAD/AGENTS.md)

### FastAPI — `unione-fastapi`

```bash
pip install unione-fastapi
```

[github.com/unione-repo/unione-fastapi](https://github.com/unione-repo/unione-fastapi), [AGENTS.md](https://github.com/unione-repo/unione-fastapi/blob/HEAD/AGENTS.md)

### Express — `unione-express`

```bash
npm install unione-express express nodemailer
```

[github.com/unione-repo/unione-express](https://github.com/unione-repo/unione-express), [AGENTS.md](https://github.com/unione-repo/unione-express/blob/HEAD/AGENTS.md)

### NestJS — `unione-nestjs`

```bash
npm install unione-nestjs nodemailer
```

[github.com/unione-repo/unione-nestjs](https://github.com/unione-repo/unione-nestjs), [AGENTS.md](https://github.com/unione-repo/unione-nestjs/blob/HEAD/AGENTS.md)

### Ruby on Rails — `unione-rails`

```bash
bundle add unione-rails
bin/rails generate unione:install  # delivery method, config/initializers/unione.rb
```

[github.com/unione-repo/unione-rails](https://github.com/unione-repo/unione-rails), [AGENTS.md](https://github.com/unione-repo/unione-rails/blob/HEAD/AGENTS.md)

### Spring Boot — `io.unione:unione-spring-boot-starter`

```xml
# pom.xml
<dependency>
    <groupId>io.unione</groupId>
    <artifactId>unione-spring-boot-starter</artifactId>
    <version>2.3.2</version>
</dependency>
```

[github.com/unione-repo/unione-spring](https://github.com/unione-repo/unione-spring), [AGENTS.md](https://github.com/unione-repo/unione-spring/blob/HEAD/AGENTS.md)

### ASP.NET Core — `UniOne.AspNetCore`

```bash
dotnet add package UniOne.AspNetCore
```

[github.com/unione-repo/unione-aspnetcore](https://github.com/unione-repo/unione-aspnetcore), [AGENTS.md](https://github.com/unione-repo/unione-aspnetcore/blob/HEAD/AGENTS.md)

### Go net/http — `github.com/unione-repo/unione-nethttp`

```bash
go get github.com/unione-repo/unione-nethttp
```

[github.com/unione-repo/unione-nethttp](https://github.com/unione-repo/unione-nethttp), [AGENTS.md](https://github.com/unione-repo/unione-nethttp/blob/HEAD/AGENTS.md)

### axum — `unione-axum`

```bash
cargo add unione-axum unione-rust-sdk
```

[github.com/unione-repo/unione-axum](https://github.com/unione-repo/unione-axum), [AGENTS.md](https://github.com/unione-repo/unione-axum/blob/HEAD/AGENTS.md)
