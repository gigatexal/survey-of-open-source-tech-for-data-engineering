# General Idea

The idea is to create a service (command-line) only for now that can create fake data for use in a data-streaming context to trial various approaches.

The goal is to model a book store.

# Schema

Customer
---
id: uuid
first_name:  string
last_name: string
birth_date: date
registered_at: timestamp
deactivated_at: timestamp
email: string

Book
---
id: uuid
title: string
author: string
published_edition_date: date
whole_sale_price: float
sale_price: float 
added_at: timestamp
deactivated_at: timestamp

PurchaseItem
---
id: uuid
created_at: timestamp
payment_method: ENUM(CreditCard, Cash, Check, DebitCard)
discounts_used: boolean
fk: Customer.id
tax_rate: float
price: float

Order /* one line per book sold */
---
id: uuid
order_line: int
pk: (id, order_line)
fk: PurchaseItem.id






