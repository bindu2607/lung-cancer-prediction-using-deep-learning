import pandas as pd 
import matplotlib.pyplot as plt 
import pickle

# Import necessary modules
from sklearn.model_selection import train_test_split 
from sklearn.preprocessing import StandardScaler 
from keras.models import Sequential 
from keras.layers import Dense, Dropout 
from keras.optimizers import Adam 
from keras.utils import to_categorical
from keras.callbacks import EarlyStopping 
from keras.regularizers import l2

# Load dataset
df = pd.read_csv('cancer_patient_datasets.csv')

# Mapping categorical labels to numerical values
level_mapping = {'Low': 0, 'Medium': 1, 'High': 2}
df['Level'] = df['Level'].replace(level_mapping)
 
df.to_csv('cancer_patient_datasets.csv', index=False)

# Extract features and labels
X = df.iloc[:, 2:-1].values
y = df.iloc[:, -1].values

# One-hot encode target variable
y = to_categorical(y, num_classes=3)

# Standardize features
scaler = StandardScaler()
X = scaler.fit_transform(X)

# Split dataset with stratification
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, stratify=y, random_state=42)

# Define the model using MLP
model = Sequential()
model.add(Dense(16, activation='relu', input_dim=X.shape[1], kernel_regularizer=l2(0.001)))
#model.add(Dropout(0.4))  # Increased dropout to reduce overfitting
model.add(Dense(8, activation='relu', kernel_regularizer=l2(0.001)))
#model.add(Dropout(0.4))
model.add(Dense(3, activation='softmax'))

# Compile the model
optimizer = Adam(learning_rate=0.001)
model.compile(optimizer=optimizer, loss='categorical_crossentropy', metrics=['accuracy'])

# Early stopping callback
early_stopping = EarlyStopping(monitor='val_loss', patience=3, restore_best_weights=True)

# Train the model
history = model.fit(X_train, y_train, epochs=30, batch_size=32, validation_data=(X_test, y_test), callbacks=[early_stopping], verbose=2)

# Evaluate the model
loss, accuracy = model.evaluate(X_test, y_test)
print(f'Test Accuracy: {accuracy * 100:.2f}%')

# Plot accuracy
plt.plot(history.history['accuracy'], label='Train Accuracy')
plt.plot(history.history['val_accuracy'], label='Validation Accuracy')
plt.title('Model Accuracy')
plt.ylabel('Accuracy')
plt.xlabel('Epoch')
plt.legend()
plt.show()

# Plot loss
plt.plot(history.history['loss'], label='Train Loss')
plt.plot(history.history['val_loss'], label='Validation Loss')
plt.title('Model Loss')
plt.ylabel('Loss')
plt.xlabel('Epoch')
plt.legend()
plt.show()

# Save the model
model.save('my_model.h5')

# Save the scaler object
with open('scaler.pkl', 'wb') as f:
    pickle.dump(scaler, f)
