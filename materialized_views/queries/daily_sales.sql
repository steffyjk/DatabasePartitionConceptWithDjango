SELECT
    show_date,
    theater_id,
    SUM(tickets_sold) AS total_tickets,
    SUM(revenue) AS total_revenue
FROM analytics_ticketsale
GROUP BY show_date, theater_id