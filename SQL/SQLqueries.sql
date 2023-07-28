/*creating the database*/
CREATE DATABASE city;
/*use the database that I have created*/
USE city;

/*Data imported with import wizard*/

/*Queries*/

/*Q1*/
select * from cities_clean_model limit 10;

/*Q2*/
select country_cd,
	round(avg(population),2) as 'avg_population',
	round(avg(PCT_working_high),2) as 'avg_PCT_working_high',
    round(avg(women_per_100),2) as 'avg_women_per_100',
    round(avg(Median_population_age),2) as 'avg_Median_population_age',
    round(avg(household_size),2) as 'avg_household_size',
    round(avg(pct_unemployment),2) as 'avg_pct_unemployment',
    round(avg(households_1_person),2) as 'avg_households_1_person',
    round(avg(car_1000),2) as 'avg_car_1000',
    round(avg(car_killed_1000),2) as 'avg_car_killed_1000',
    round(avg(pct_nationals),2) as 'avg_pct_nationals',
    round(avg(birth_1000),2) as 'avg_birth_1000'
from(
select
	left(citycode,2) as 'country_cd',
    population,
    PCT_working_high,
    women_per_100,
    Median_population_age,
    household_size,
    pct_unemployment,
    households_1_person,
    car_1000,
    car_killed_1000,
    pct_nationals,
    birth_1000
from cities_clean_model) intermediate
group by country_cd;

/*Q3*/
with
t1 as (select country_cd,
	round(avg(population),2) as 'avg_population'
from(
select
	left(citycode,2) as 'country_cd',
    population
from cities_clean_model) intermediate
group by country_cd
),
t2 as (
select left(ccm.citycode,2) as 'country_cd',
ccm.cities_name,
ccm.population,
t1.avg_population

from cities_clean_model ccm
left join t1 on t1.country_cd=left(ccm.citycode,2)
)
select * ,
(population - avg_population) as 'dif_pop_avg'
from  t2
order by dif_pop_avg desc;

