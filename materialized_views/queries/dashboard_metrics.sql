SELECT
    t.city,
    d.show_date,
    SUM(d.total_tickets) AS city_tickets,
    SUM(d.total_revenue) AS city_revenue
FROM daily_sales_mv d
JOIN analytics_theater t ON t.id = d.theater_id
GROUP BY t.city, d.show_date