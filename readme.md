# Hal yang perlu di tambahkan

1. bagaimana cara penerapan DNSSEC
2. bagaimana cara melakukan SSH KEY di VPS

# Jalur Belajar yang Ideal

1. Mulai dari Caddy
2. Sudah paham reverse proxy
3. Pindah ke Nginx kalau butuh tuning
4. Pakai Traefik kalau masuk microservices

| Kebutuhan                 | Gunakan         |
| ------------------------- | --------------- |
| Pemula                    | Caddy           |
| Microservices             | Traefik         |
| High performance tuning   | Nginx           |
| Enterprise load balancing | HAProxy / Envoy |
| Network caching/filtering | Squid           |


# 🔥 Kapan Perlu SSL di Dev?

Wajib SSL kalau:
1. Testing OAuth (Google login, dll)
2. Testing payment gateway
3. Testing cookie secure
4. Testing PWA / service worker
5. API butuh HTTPS