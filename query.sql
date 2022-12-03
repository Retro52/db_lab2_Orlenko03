SELECT launchyear.launchy_year, COUNT(cpu_name) FROM cpu INNER JOIN launchyear
ON launchyear.launchy_id = cpu.launchy_id
GROUP BY launchyear.launchy_year
ORDER BY launchyear.launchy_year DESC

SELECT threads.thread_count, COUNT(cpu_name) FROM cpu INNER JOIN threads
ON threads.thread_id = cpu.thread_id
GROUP BY threads.thread_count
ORDER BY COUNT(cpu_name), threads.thread_count

SELECT launchyear.launchy_year, MIN(lithography.lithography_size)
FROM cpu
JOIN launchyear
ON launchyear.launchy_id = cpu.launchy_id
JOIN lithography
ON lithography.lithography_id = cpu.lithography_id
GROUP BY launchyear.launchy_year
