# General Idea

The idea is to create a service (command-line) only for now that can create fake data for use in a data-streaming context to trial various approaches.

The goal is to model a book store.

# Schema

Customer
---
pk: uuid
first_name:  string
last_name: string
birth_date: date
registered_at: timestamp
deactivated_at: timestamp
email: string

Book
---
pk: uuid
title: string
author: string
published_edition_date: date
whole_sale_price: int # pennies i.e 100 = 100 usd
sale_price: int # pennies i.e 100 = 1 dollar usd
added_at: timestamp
deactivated_at: timestamp

PurchaseItem
---
pk: uuid
created_at: timestamp
payment_method: ENUM(CreditCard, Cash, Check, DebitCard)
discounts_used: boolean

Order /* one line per book sold by 
---
pk: uuid
fk: PurchaesItem.pk




