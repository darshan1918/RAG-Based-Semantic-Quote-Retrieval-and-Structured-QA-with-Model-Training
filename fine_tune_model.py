# # fine_tune_model.py
# from sentence_transformers import SentenceTransformer, losses, InputExample
# from torch.utils.data import DataLoader

# # # Load base model
# # model = SentenceTransformer('all-MiniLM-L6-v2')

# # # Prepare data
# # train_examples = [InputExample(texts=[row["quote"]], label=1.0) for _, row in df.iterrows()]
# # train_dataloader = DataLoader(train_examples, batch_size=16)
# # train_loss = losses.CosineSimilarityLoss(model)

# # # Fine-tune
# # model.fit(train_objectives=[(train_dataloader, train_loss)], epochs=1, warmup_steps=10)


# model = SentenceTransformer('all-MiniLM-L6-v2')
# # Save model
# model.save("fine_tuned_quotes_model")
