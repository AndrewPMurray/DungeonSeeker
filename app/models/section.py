from .db import db

class Section(db.Model):
    __tablename__ = 'sections'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    campaign_id = db.Column(db.Integer, db.ForeignKey('campaigns.id'), nullable=False)
    
    campaign = db.relationship("Campaign", back_populates="sections")
    articles = db.relationship("Article", back_populates="section", cascade="all, delete")

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'articles': [article.to_dict() for article in self.articles]
        }
