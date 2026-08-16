.PHONY: dev-web dev-api infra-up infra-down infra-logs

dev-web:
	npm run dev:web

dev-api:
	cd apps/api && uv run fastapi dev src/app/main.py --host 0.0.0.0 --port 8001

infra-up:
	docker compose up -d

infra-down:
	docker compose down

infra-logs:
	docker compose logs -f