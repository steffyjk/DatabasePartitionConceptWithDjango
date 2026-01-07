SELECT
    city,
    COUNT(DISTINCT show_date) AS active_days,
    SUM(city_tickets) AS tickets,
    SUM(city_revenue) AS revenue
FROM theater_daily_summary_mv
GROUP BY city