# -*- coding: utf-8 -*-
"""User models."""
import datetime as dt

from flask_login import UserMixin

from my_flask_app.database import Column, PkModel, db, reference_col, relationship
from my_flask_app.extensions import bcrypt


class Role(PkModel):
    """A role for a user."""
    
    __tablename__ = "roles"
    __table_args__ = {'extend_existing': True} 
    name = Column(db.String(80), unique=True, nullable=False)
    user_id = reference_col("users", nullable=True)
    user = relationship("User", backref="roles")

    def __init__(self, name, **kwargs):
        """Create instance."""
        super().__init__(name=name, **kwargs)

    def __repr__(self):
        """Represent instance as a unique string."""
        return f"<Role({self.name})>"


class User(UserMixin, PkModel):
    """A user of the app."""

    __tablename__ = "users"
    __table_args__ = {'extend_existing': True} 
    username = Column(db.String(80), unique=True, nullable=False)
    email = Column(db.String(80), unique=True, nullable=False)
    #: The hashed password
    password = Column(db.LargeBinary(128), nullable=True)
    created_at = Column(db.DateTime, nullable=False, default=dt.datetime.utcnow)
    first_name = Column(db.String(30), nullable=True)
    last_name = Column(db.String(30), nullable=True)
    active = Column(db.Boolean(), default=False)
    is_admin = Column(db.Boolean(), default=False)

    def __init__(self, username, email, password=None, **kwargs):
        """Create instance."""
        super().__init__(username=username, email=email, **kwargs)
        if password:
            self.set_password(password)
        else:
            self.password = None

    def set_password(self, password):
        """Set password."""
        self.password = bcrypt.generate_password_hash(password)

    def check_password(self, value):
        """Check password."""
        return bcrypt.check_password_hash(self.password, value)

    @property
    def full_name(self):
        """Full user name."""
        return f"{self.first_name} {self.last_name}"

    def __repr__(self):
        """Represent instance as a unique string."""
        return f"<User({self.username!r})>"

class Cost(PkModel):
    """A user of the app."""

    __tablename__ = "costs"
    __table_args__ = {'extend_existing': True} 
    product_name = Column(db.String(80), nullable=False)
    product_type = Column(db.String(80))
    cost = Column(db.Integer(), unique=False, nullable=False)
    price = Column(db.Integer(), nullable=True, default=0)
    shipping= Column(db.Integer(), nullable=True, default=.40)
    incoming_traffic = Column(db.Integer(), nullable=True, default=0)
    take_rate = Column(db.Integer(), nullable=True, default=0)
    total_revenue = Column(db.Integer(), nullable=True, default=0)
    total_orders = Column(db.Integer(), nullable=True, default=0)
    products_offered = Column(db.Integer(), nullable=True, default=0)
    up_cost_avg = Column(db.Integer(), nullable=True, default=0)
    funnel_id = Column(db.Integer(), db.ForeignKey('funnels.id', ondelete="CASCADE"))
    funnel = relationship("Funnel", back_populates="product")


    @property
    def __repr__(self):
        """Represent instance as a unique string."""
        return f"<Cost({self.product_name!r})>"

class Funnel(PkModel):
    """A user of the app."""

    __tablename__ = "funnels"
    __table_args__ = {'extend_existing': True} 
    funnel_name = Column(db.String(80), unique=True, nullable=False)
    shipping_cost = Column(db.Integer())
    callcenter_cost = Column(db.Integer())
    advertising_cost = Column(db.Integer())
    fe_percent = Column(db.Integer())
    traffic = Column(db.Integer())
    has_salespage = Column(db.Boolean())
    product = relationship(
        "Cost", back_populates="funnel",
        cascade="all, delete",
        passive_deletes=True
    )


    @property
    def __repr__(self):
        """Represent instance as a unique string."""
        return f"<Cost({self.funnel_name!r})>"

class Orders(PkModel):
    """A user of the app."""

    __tablename__ = "orders"
    funnel_id = Column(db.String(80), unique=True, nullable=False)
    product_id = Column(db.Integer(), unique=False, nullable=False)
    product_cost = Column(db.Integer(), unique=False, nullable=False)
    date_inserted = Column(db.Date(), nullable=True)
    


    @property
    def __repr__(self):
        """Represent instance as a unique string."""
        return f"<Order({self.funnel_name!r})>"