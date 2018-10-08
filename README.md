# mx-ocr

This project uses Google Cloud Vision to detect document text.

### Configuration

Function output is configured in the `config.json` file.

### Deployment

```bash
gcloud beta functions deploy ocr-extract \
  --runtime python37 \
  --trigger-bucket gs://mx-docs \
  --entry-point extract_text
```

### View Log Output

```bash
gcloud beta functions logs read ocr-extract
```
